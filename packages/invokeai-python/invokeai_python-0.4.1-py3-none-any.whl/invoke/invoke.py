# Path: invoke\invoke.py
import asyncio
import aiohttp
from typing import List, Optional
from .api.utilities import UtilitiesApi
from .api.models import ModelsApi, ModelInstallJobStatus
from .api.images import ImagesApi
from .api.boards import BoardsApi
from .api.app import AppApi
from .api.queue import QueueApi, EnqueueBatch
from .api.download_queue import DownloadQueueApi


class Invoke:
    _client: aiohttp.ClientSession

    host: str
    utilities: UtilitiesApi
    models: ModelsApi
    images: ImagesApi
    boards: BoardsApi
    app: AppApi
    queue: QueueApi
    downloadQueue: DownloadQueueApi


    def __init__(self, host: str = "http://127.0.0.1:9090",):
        self._client = aiohttp.ClientSession()
        self.host = host
        self.utilities = UtilitiesApi(self._client, host)
        self.models = ModelsApi(self._client, host)
        self.images = ImagesApi(self._client, host)
        self.boards = BoardsApi(self._client, host)
        self.app = AppApi(self._client, host)
        self.queue = QueueApi(self._client, host)
        self.downloadQueue = DownloadQueueApi(self._client, host)


    def __del__(self):
        if self._client:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(self._client.close())
            else:
                loop.run_until_complete(self._client.close())
            self._client = None


    async def wait_invoke(self, delay: float = 0.1) -> str:
        while True:
            try:
                version = await self.app.version()
                return version.version
            except Exception:
                await asyncio.sleep(delay)


    async def wait_batch(self, batch: EnqueueBatch, delay: float = 0.1) -> None:
        batch_id = batch.batch.batch_id
        while True:
            await asyncio.sleep(delay)

            status = await self.queue.get_batch_status(batch_id)

            if status.failed == 1:
                # queue_list = await self.invoke.queue.list(limit=100)
                # error = queue_list.items[-1].error
                raise Exception("Batch error")

            if status.canceled == 1:
                raise Exception("Batch canceled")

            if status.completed == 1:
                break


    async def wait_install_models(self, ids: Optional[List[int]] = None, delay: float = 0.5, raise_on_error: bool = False) -> None:
        while True:
            queue = await self.models.list_install_jobs()
            if ids is not None:
                queue = [job for job in queue if job.id in ids]

            statuses = [job.status for job in queue]

            if raise_on_error:
                errors = [f"Path: {job.source}" for job in queue if job.status == ModelInstallJobStatus.error]
                if errors:
                    raise RuntimeError("One or more jobs failed with errors:\n" + "\n".join(errors))

            if all(status in {ModelInstallJobStatus.completed, ModelInstallJobStatus.cancelled} for status in statuses):
                return
            
            await asyncio.sleep(delay)