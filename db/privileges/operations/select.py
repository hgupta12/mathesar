from sqlalchemy import select

from db.utils import execute_statement, get_pg_catalog_table


def fetch_db_privileges(engine, metadata):
    pg_role_table = get_pg_catalog_table('pg_roles', engine, metadata)
    role_privileges_sel = select(pg_role_table.rolsuper, pg_role_table.rolcreaterole, pg_role_table.rolcreatedb, pg_role_table.rolcanlogin)
    return execute_statement(engine, role_privileges_sel)
