"""Dependency injection container"""

__author__ = 'infast1k'

from functools import cache

from motor.motor_asyncio import AsyncIOMotorClient

from punq import Container, Scope

from application.command.folder.create_folder import CreateFolderCommand, CreateFolderCommandHandler

from composition.mediator.main import Mediator

from domain.folder.repository import BaseFolderRepository

from infrastructure.repository.folder.mongo import MongoDBFolderRepository


@cache
def init_container() -> Container:
    """Initialize dependency injection container"""
    container = Container()

    def create_mongodb_client() -> AsyncIOMotorClient:
        return AsyncIOMotorClient(
            # FIXME: read from config
            'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin',
            serverSelectionTimeoutMS=3000,
        )

    container.register(AsyncIOMotorClient, factory=create_mongodb_client, scope=Scope.singleton)
    mongo_db_client = container.resolve(AsyncIOMotorClient)

    def init_folder_mongodb_repository() -> BaseFolderRepository:
        return MongoDBFolderRepository(
            client=mongo_db_client,
            # FIXME: read from config
            db_name='{MONGO_FOLDER_DB_NAME}',
            # FIXME: read from config
            collection_name='{MONGO_FOLDER_COLLECTION}',
        )

    container.register(BaseFolderRepository, factory=init_folder_mongodb_repository, scope=Scope.singleton)

    # Mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        create_folder_command_handler = CreateFolderCommandHandler(
            folder_repository=container.resolve(BaseFolderRepository),
        )

        mediator.register_command(CreateFolderCommand, create_folder_command_handler)

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
