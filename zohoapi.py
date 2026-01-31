import requests
import re
import time
import json
import os
OAUTH_URL = "https://accounts.zoho.com/"
MAIL_API_URL = "https://mail.zoho.com/api/"


class ZohoMailAPI:
    def __init__(self, config_path=None):
            self.access_token = None
            
            if config_path:
                self.config_path = config_path
            else:
                self.config_path = "config_zoho.json"
            
            self.config = self._load_config(self.config_path)
            
            self.client_id = self.config.get("client_id")
            self.client_secret = self.config.get("client_secret")
            self.refresh_token = self.config.get("refresh_token")
            self.account_id = self.config.get("account_id")
    def _load_config(self, path):
        """Hàm phụ trợ để đọc file JSON"""
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Không tìm thấy file cấu hình tại: {path}")
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[-] Lỗi khi đọc file config: {e}")
            return {}
    def refresh_access_token(self):
        """Hàm cấp lại Access Token"""
        url = f"{OAUTH_URL}oauth/v2/token"
        data = {
                    "refresh_token": self.refresh_token,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "grant_type": "refresh_token"
                }
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                result = response.json()
                self.access_token = result.get("access_token")
                print("=> Access Token mới đã sẵn sàng.", self.access_token)
                return True
            else:
                print(f"=> Lỗi cấp Token: {response.text}")
                return False
        except Exception as e:
            print(f"=> Lỗi kết nối Token: {e}")
            return False

    def step2_get_emails(self,target_email):
            """BƯỚC 2: Tải danh sách email dựa trên tìm kiếm cụ thể ( ở đây là kiếm theo email)"""
            if not self.access_token:
                print(f"[{time.strftime('%H:%M:%S')}] Lỗi: Chưa có Access Token.")
                return []

            print(f"[{time.strftime('%H:%M:%S')}] Bước 2: Đang tìm kiếm email với tiêu đề 'entire:{target_email}'...")
            
            url = f"https://mail.zoho.com/api/accounts/{self.account_id}/messages/search"
            
            headers = {
                "Authorization": f"Zoho-oauthtoken {self.access_token}",
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            
            params = {
                "searchKey": f"entire:{target_email}",
                "start": 1,
                "limit": 20
            }

            try:
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    emails = data.get("data", [])
                    
                    if not emails:
                        print("    => Kết quả: Không tìm thấy email nào khớp với tìm kiếm.")
                    else:
                        print(f"    => Thành công! Tìm thấy {len(emails)} email phù hợp.")
                        print("    => Danh sách email đã tải về.",emails)
                    return emails
                else:
                    print(f"    => Lỗi API ({response.status_code}): {response.text}")
                    return []
                    
            except Exception as e:
                print(f"    => Lỗi khi kết nối lấy email: {e}")
                return []

    def step3_get_full_content(self, message_id):
        """BƯỚC 3: Truy cập hiện thị nội dung gốc (Yêu cầu Message ID)"""
        print(f"[{time.strftime('%H:%M:%S')}] Bước 3: Đang đọc nội dung chi tiết...")
        print(f"    => MessageID: {message_id}")
        
        url = f"{MAIL_API_URL}accounts/{self.account_id}/messages/{message_id}/originalmessage"
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Zoho-oauthtoken {self.access_token}"
        }
        
        try:
            res = requests.get(url, headers=headers).json()
            content = res.get("data", {}).get("content", "")
            return content
        except Exception as e:
            print(f"    => Lỗi khi đọc nội dung email: {e}")
            return ""
    def step4_code_15converse(self, text):
            """BƯỚC 4: Tìm mã code Converse dạng WELCOME-XXXX..."""
            print(f"[{time.strftime('%H:%M:%S')}] Bước 4 (Converse): Đang phân tích HTML để tìm code...")
            
            match = re.search(r"WELCOME-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}", text)

            if match:
                found_code = match.group(0) 
                print(f"    => ✅ Đã tìm thấy code: {found_code}")
                return found_code
            else:
                print("    => ❌ Không tìm thấy định dạng code Converse (WELCOME-...).")
                return None
            
