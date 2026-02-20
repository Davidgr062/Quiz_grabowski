from app import app

def test_index():
    with app.test_client() as client:
        resp = client.get('/')
        print('status_code:', resp.status_code)
        # print a short preview of the response body for quick verification
        body = resp.data.decode(errors='replace')
        print('body_preview:', body[:300].replace('\n', ' '))

if __name__ == '__main__':
    test_index()
