#!/usr/bin/env python3
"""
測試 DigitalOcean PostgreSQL 連接並建立 churchdb 資料庫
"""
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def load_env():
    """載入 .env 檔案中的環境變數"""
    env_vars = {}
    try:
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key] = value
        return env_vars
    except FileNotFoundError:
        print("錯誤：找不到 .env 檔案")
        return {}

def test_connection():
    """測試資料庫連接"""
    env_vars = load_env()
    
    # 連接參數
    connection_params = {
        'host': env_vars.get('DB_HOST'),
        'port': env_vars.get('DB_PORT'),
        'user': env_vars.get('DB_USERNAME'),
        'password': env_vars.get('DB_PASSWORD'),
        'database': env_vars.get('DB_ORIGINAL_NAME', 'defaultdb'),  # 先連接到原始資料庫
        'sslmode': env_vars.get('DB_SSLMODE', 'require')
    }
    
    print("正在測試資料庫連接...")
    print(f"主機: {connection_params['host']}")
    print(f"端口: {connection_params['port']}")
    print(f"用戶: {connection_params['user']}")
    print(f"資料庫: {connection_params['database']}")
    
    try:
        # 建立連接
        conn = psycopg2.connect(**connection_params)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        print("✅ 資料庫連接成功！")
        
        # 檢查當前資料庫版本
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        print(f"PostgreSQL 版本: {version}")
        
        # 檢查是否已存在 churchdb
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'churchdb';")
        exists = cursor.fetchone()
        
        if exists:
            print("⚠️  churchdb 資料庫已存在")
        else:
            print("正在建立 churchdb 資料庫...")
            cursor.execute("CREATE DATABASE churchdb;")
            print("✅ churchdb 資料庫建立成功！")
        
        # 列出所有資料庫
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = cursor.fetchall()
        print("\n現有資料庫:")
        for db in databases:
            print(f"  - {db[0]}")
        
        cursor.close()
        conn.close()
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ 資料庫連接失敗: {e}")
        return False
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")
        return False

def test_churchdb_connection():
    """測試連接到新建立的 churchdb"""
    env_vars = load_env()
    
    connection_params = {
        'host': env_vars.get('DB_HOST'),
        'port': env_vars.get('DB_PORT'),
        'user': env_vars.get('DB_USERNAME'),
        'password': env_vars.get('DB_PASSWORD'),
        'database': 'churchdb',
        'sslmode': env_vars.get('DB_SSLMODE', 'require')
    }
    
    print("\n正在測試 churchdb 連接...")
    
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()
        
        print("✅ churchdb 連接成功！")
        
        # 檢查資料庫是否為空
        cursor.execute("""
            SELECT COUNT(*) 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """)
        table_count = cursor.fetchone()[0]
        print(f"churchdb 中的表格數量: {table_count}")
        
        cursor.close()
        conn.close()
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ churchdb 連接失敗: {e}")
        return False

if __name__ == "__main__":
    print("=== DigitalOcean PostgreSQL 連接測試 ===\n")
    
    # 測試連接並建立資料庫
    if test_connection():
        # 測試新資料庫連接
        test_churchdb_connection()
        print("\n✅ 所有測試完成！")
    else:
        print("\n❌ 連接測試失敗，請檢查連接參數")
