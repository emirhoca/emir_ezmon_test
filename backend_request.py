
import sqlite3
import requests

def update_testmon_run_id(db_path, run_id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Insert run id if not existing
        cursor.execute(
            "INSERT OR IGNORE INTO run_uid (id) VALUES (?)",
            (run_id,)
        )

        # Update only NULL values
        cursor.execute(
            "UPDATE run_infos SET run_uid = ? WHERE run_uid IS NULL",
            (run_id,)
        )

        affected = cursor.rowcount
        conn.commit()

        return affected

    except Exception as e:
        # ---- ERROR LOG ----
       
        return None

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    
    #update_testmon_run_id(".testmondata" ,"1907")
    url = "http://localhost:8000/api/client/upload"
    files = {'file': open('.testmondata', 'rb')}
    data = {
        'repo_id': 'emir_repo_new',
        'job_id': 'emir_job_new',
        'run_id': '1910'
    }
    response = requests.post(url, files=files, data=data)

    print(response.text)