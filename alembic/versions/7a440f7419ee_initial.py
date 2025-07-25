"""initial

Revision ID: 7a440f7419ee
Revises: 729ff192b975
Create Date: 2025-06-29 18:13:48.232002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a440f7419ee'
down_revision: Union[str, Sequence[str], None] = '729ff192b975'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gudang',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nama', sa.String(), nullable=False),
    sa.Column('lokasi', sa.String(), nullable=True),
    sa.Column('keterangan', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gudang_id'), 'gudang', ['id'], unique=False)
    op.create_table('kategori',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nama', sa.String(), nullable=False),
    sa.Column('deskripsi', sa.String(), nullable=False),
    sa.Column('id_gudang', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_gudang'], ['gudang.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_kategori_id'), 'kategori', ['id'], unique=False)
    op.create_table('pengguna',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nama_lengkap', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.Enum('user', 'admin', name='role_enum'), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.Column('sign_status', sa.Boolean(), nullable=False),
    sa.Column('id_gudang', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_gudang'], ['gudang.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_pengguna_id'), 'pengguna', ['id'], unique=False)
    op.create_table('barang',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('kd_barang', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('deskripsi', sa.String(), nullable=True),
    sa.Column('satuan', sa.Enum('psc', 'kg', 'liter', name='satuan_enum'), nullable=False),
    sa.Column('harga_beli', sa.DECIMAL(), nullable=False),
    sa.Column('harga_jual', sa.DECIMAL(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('id_kategori', sa.String(), nullable=True),
    sa.Column('id_gudang', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_gudang'], ['gudang.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_kategori'], ['kategori.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_barang_id'), 'barang', ['id'], unique=False)
    op.create_index(op.f('ix_barang_kd_barang'), 'barang', ['kd_barang'], unique=False)
    op.create_table('log_aktivitas',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('waktu', sa.DateTime(), nullable=True),
    sa.Column('aksi', sa.String(), nullable=False),
    sa.Column('keterangan', sa.String(), nullable=False),
    sa.Column('entitas', sa.String(), nullable=False),
    sa.Column('id_entitas', sa.String(), nullable=False),
    sa.Column('before_data', sa.JSON(), nullable=False),
    sa.Column('after_data', sa.JSON(), nullable=False),
    sa.Column('id_pengguna', sa.String(), nullable=False),
    sa.Column('id_gudang', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_gudang'], ['gudang.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_pengguna'], ['pengguna.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_log_aktivitas_id'), 'log_aktivitas', ['id'], unique=False)
    op.create_table('supplier',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nama', sa.String(), nullable=False),
    sa.Column('telepon', sa.String(), nullable=False),
    sa.Column('alamat', sa.String(), nullable=False),
    sa.Column('id_barang', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_barang'], ['barang.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_barang')
    )
    op.create_index(op.f('ix_supplier_id'), 'supplier', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_supplier_id'), table_name='supplier')
    op.drop_table('supplier')
    op.drop_index(op.f('ix_log_aktivitas_id'), table_name='log_aktivitas')
    op.drop_table('log_aktivitas')
    op.drop_index(op.f('ix_barang_kd_barang'), table_name='barang')
    op.drop_index(op.f('ix_barang_id'), table_name='barang')
    op.drop_table('barang')
    op.drop_index(op.f('ix_pengguna_id'), table_name='pengguna')
    op.drop_table('pengguna')
    op.drop_index(op.f('ix_kategori_id'), table_name='kategori')
    op.drop_table('kategori')
    op.drop_index(op.f('ix_gudang_id'), table_name='gudang')
    op.drop_table('gudang')
    # ### end Alembic commands ###
