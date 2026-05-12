"""
Inspeciona tabelas e registros do PostgreSQL do SGQ.
Uso: python db_inspector.py
Requer: psycopg2-binary e variáveis de ambiente configuradas.
"""
import os
import psycopg2

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "sgq_database")
DB_USER = os.getenv("DB_USER", "sgq_user")
DB_PASS = os.getenv("DB_PASS", "sgq_password")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST, port=DB_PORT,
        dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )


def list_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_name FROM information_schema.tables
                WHERE table_schema = 'public' ORDER BY table_name;
            """)
            tables = cur.fetchall()
    print("Tabelas disponíveis:")
    for t in tables:
        print(f"  - {t[0]}")


def count_ocorrencias():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM core_ocorrencia;")
            total = cur.fetchone()[0]
    print(f"Total de ocorrências registradas: {total}")


if __name__ == "__main__":
    list_tables()
    count_ocorrencias()
