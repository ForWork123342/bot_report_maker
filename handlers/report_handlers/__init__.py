__all__ = ("router")

from aiogram import Router
from . import worker, product, packaging, weight, finish, send_data, delete_night_report

router = Router()
router.include_router(worker.router)
router.include_router(product.router)
router.include_router(packaging.router)
router.include_router(weight.router)
router.include_router(finish.router)
router.include_router(send_data.router)
router.include_router(delete_night_report.router)