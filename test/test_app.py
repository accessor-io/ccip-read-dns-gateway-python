import json
import pytest
from app import db, DNSQuery

def test_index_page(client):
    """Test if the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Enter DNS Query' in response.data

def test_dns_query(client):
    """Test the DNS query functionality."""
    data = {
        'domains': 'example.com\nexample.org',
        'qtype': 1
    }
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Current Results' in response.data

def test_db_entry(client):
    """Test if the DNS query results are saved in the database."""
    data = {
        'domains': 'example.com\nexample.org',
        'qtype': 1
    }
    client.post('/', data=data)

    with client.application.app_context():
        queries = DNSQuery.query.all()
        assert len(queries) == 2
        assert queries[0].name == 'example.com'
        assert queries[1].name == 'example.org'
