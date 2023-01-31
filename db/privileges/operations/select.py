from sqlalchemy import func, select

from db.utils import execute_statement, get_pg_catalog_table


def fetch_db_privileges(engine, metadata):
    pg_role_table = get_pg_catalog_table('pg_roles', engine, metadata)
    role_privileges_sel = select(pg_role_table.c.rolsuper, pg_role_table.c.rolcreaterole, pg_role_table.c.rolcreatedb, pg_role_table.c.rolcanlogin)
    return execute_statement(engine, role_privileges_sel)


def fetch_schema_privileges(engine, metadata):
    pg_namespace = get_pg_catalog_table('pg_namespace', engine, metadata)
    schema_sel = select(pg_namespace.c.oid, pg_namespace.c.nspname.label("name")).where(pg_namespace.c.nspname.regexp_match('^(?!pg_)'), pg_namespace.c.nspname != 'information_schema').cte()
    schema_privileges_select = select(schema_sel.c.oid, schema_sel.c.name, func.has_schema_privilege(func.current_user(), schema_sel.c.name, 'CREATE'))
    stmt = execute_statement(engine, schema_privileges_select)
    return stmt.fetchall()
