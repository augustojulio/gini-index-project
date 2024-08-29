import os
from dotenv import load_dotenv
from alembic import context
from sqlalchemy import engine_from_config, pool
from app.models import GiniIndex  # Atualizado para refletir o caminho correto

# Load environment variables from .env file
load_dotenv()

config = context.config

# Set up SQLAlchemy URL
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

# Setup for Alembic
target_metadata = GiniIndex.metadata

def run_migrations_offline():
    url = config.get_main_option('sqlalchemy.url')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
