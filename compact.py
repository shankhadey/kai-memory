#!/usr/bin/env python3
"""
Kai Memory Compaction Script
- Deduplicates by ID (keeps latest timestamp per ID)
- Removes tombstoned records
- Archives old closed tasks (optional)
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

MEMORY_FILE = Path(__file__).parent.parent / "memory.jsonl"
ARCHIVE_DIR = Path(__file__).parent.parent / "archive"

def load_records(filepath):
    records = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

def compact(records, archive_days=90):
    """Keep latest record per ID, remove tombstones, archive old closed tasks."""
    by_id = {}
    cutoff = datetime.utcnow() - timedelta(days=archive_days)
    archived = []
    
    for r in records:
        rid = r.get('id')
        if not rid:
            continue
        
        # Skip tombstones
        if r.get('status') == 'tombstone':
            continue
        
        # Check if should archive (closed task older than cutoff)
        if r.get('type') == 'task' and r.get('status') == 'done':
            ts = datetime.fromisoformat(r['ts'].replace('Z', '+00:00'))
            if ts.replace(tzinfo=None) < cutoff:
                archived.append(r)
                continue
        
        # Keep latest by timestamp
        existing = by_id.get(rid)
        if existing:
            existing_ts = existing.get('ts', '')
            new_ts = r.get('ts', '')
            if new_ts > existing_ts:
                by_id[rid] = r
        else:
            by_id[rid] = r
    
    return list(by_id.values()), archived

def save_records(filepath, records):
    with open(filepath, 'w') as f:
        for r in records:
            f.write(json.dumps(r, separators=(',', ':')) + '\n')

def save_archive(archived):
    if not archived:
        return
    ARCHIVE_DIR.mkdir(exist_ok=True)
    archive_file = ARCHIVE_DIR / f"archive-{datetime.utcnow().strftime('%Y-%m')}.jsonl"
    with open(archive_file, 'a') as f:
        for r in archived:
            f.write(json.dumps(r, separators=(',', ':')) + '\n')

def main():
    if not MEMORY_FILE.exists():
        print("No memory.jsonl found")
        sys.exit(1)
    
    records = load_records(MEMORY_FILE)
    before_count = len(records)
    
    compacted, archived = compact(records)
    after_count = len(compacted)
    
    save_records(MEMORY_FILE, compacted)
    save_archive(archived)
    
    print(f"Compacted: {before_count} → {after_count} records")
    if archived:
        print(f"Archived: {len(archived)} old closed tasks")

if __name__ == "__main__":
    main()
