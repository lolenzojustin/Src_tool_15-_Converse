import sys
import os
from datetime import datetime
import json
from dotenv import load_dotenv, set_key
import requests
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import random
import uuid
import string
import zohoapi
import re



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_external_path(filename):
    if getattr(sys, 'frozen', False):

        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, filename)
HISTORY_FILE = get_external_path("check_Code15%Converse.txt")
class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(950, 831)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget.setWindowIcon(icon)

        Widget.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Widget)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setStyleSheet("background-color: #f1c40f; /* Màu vàng Gold */\n"
"color: black;              /* Chữ màu đen để tương phản tốt với nền vàng */\n"
"border-radius: 5px;        /* Bo góc */\n"
"border: 1px solid #f39c12; /* Viền màu vàng đậm hơn */\n"
"font-weight: bold;         /* Chữ đậm */")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: #cccccc;\n"
"color: black;\n"
"")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setStyleSheet("background-color: #cccccc;\n"
"color: black;\n"
"")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: #999999;\n"
"color: black;")
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_7.addWidget(self.lineEdit_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setStyleSheet("background-color: #999999;\n"
"color: black;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 3)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #2ecc71; /* Màu xanh lá cây */\n"
"color: white;              /* Chữ màu trắng cho dễ đọc */\n"
"border-radius: 5px;        /* Bo góc cho giống các nút phía trên */\n"
"border: 1px solid #27ae60; /* Viền màu xanh đậm hơn một chút */\n"
"font-weight: bold;         /* Chữ đậm */")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: #e74c3c; /* Màu đỏ đậm vừa phải */\n"
"color: white;              /* Chữ màu trắng */\n"
"border-radius: 5px;        /* Bo góc giống các nút trên */\n"
"border: 1px solid #c0392b; /* Viền màu đỏ sẫm hơn */\n"
"font-weight: bold;         /* Chữ đậm */")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txt_log = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_log.setMinimumSize(QtCore.QSize(0, 260))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txt_log.setFont(font)
        self.txt_log.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.txt_log.setReadOnly(True)
        self.txt_log.setObjectName("txt_log")
        self.horizontalLayout_5.addWidget(self.txt_log)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        Widget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Widget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        Widget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Widget)
        self.statusbar.setObjectName("statusbar")
        Widget.setStatusBar(self.statusbar)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Tool lấy code 15% Converse"))
        self.pushButton_2.setStyleSheet(_translate("Widget", "QPushButton {\n"
"    background-color: #1e90ff;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #187bcd;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #145ea8;\n"
"}\n"
""))
        self.pushButton_2.setText(_translate("Widget", "Bắt đầu lấy code"))
        self.pushButton.setText(_translate("Widget", "Mở lịch sử file lấy code"))
        self.lineEdit_2.setStyleSheet(_translate("Widget", "background-color: #cccccc;\n"
"color: black;\n"
""))
        self.lineEdit_2.setText(_translate("Widget", "Key_CapTra ->>>"))
        self.lineEdit_4.setStyleSheet(_translate("Widget", "background-color: #cccccc;\n"
"color: black;\n"
""))
        self.lineEdit_4.setText(_translate("Widget", "Không cần"))
        self.lineEdit_3.setStyleSheet(_translate("Widget", "background-color: #999999;\n"
"color: black;\n"
""))
        self.lineEdit_3.setText(_translate("Widget", "Đường dẫn file proxy ->>>"))
        self.lineEdit.setStyleSheet(_translate("Widget", "background-color: #999999;\n"
"color: black;\n"
""))
        self.lineEdit_5.setText(_translate("Widget", "Phiên Bản ->>>"))
        self.lineEdit_7.setText(_translate("Widget", "số 1"))
        self.lineEdit_8.setText(_translate("Widget", "Đường dẫn file domain ->>"))
        self.pushButton_3.setText(_translate("Widget", "TIẾP TỤC"))
        self.pushButton_4.setText(_translate("Widget", "DỪNG LẠI"))
        self.txt_log.setStyleSheet(_translate("Widget", "QTextEdit {\n"
"    color: lime;\n"
"    background-color: black;\n"
"    font-family: Consolas;\n"
"    font-size: 10pt;\n"
"}\n"
""))
        self.txt_log.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">XEM TIẾN TRÌNH, THÔNG BÁO TẠI ĐÂY !</p></body></html>"))



class MultiThread(QThread):
    result = pyqtSignal(str)
    log = pyqtSignal(str)
    task_completed = pyqtSignal() 

    def __init__(self, path=None, proxy=None, access_token=None):
        super().__init__()
        self.path = path
        self.proxy = proxy
        self.access_token = access_token
        self.apiZoho = None   
        
    def startCheckBalance(self):
        try:
            ip, port, username, password = self.proxy.split(":")
            proxy_dict = {"http": f"http://{username}:{password}@{ip}:{port}", "https": f"http://{username}:{password}@{ip}:{port}"}
            self.log.emit("🔄 Đang chạy luồng mới...")
            V_Chrome = random.choice(["140", "141", "142", "143"])
            char_set = string.ascii_lowercase + string.digits 
            random_prefix = ''.join(random.choices(char_set, k=12))
            email_random = f"{random_prefix}@aieduvn.com"
            list_prefixes = ["971-471", "503-261", "781-526", "206-253"]
            full_phone = f"{random.choice(list_prefixes)}-{''.join(random.choices(string.digits, k=4))}"
            first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica"]
            last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson"]

            random_first_name = random.choice(first_names)
            random_last_name = random.choice(last_names)
            r_year = random.randint(1980, 2005)  
            r_month = random.randint(1, 12)      
            r_day = random.randint(1, 29)        

            formatted_dob = f"{r_year}-{r_month:02d}-{r_day:02d}"

            str_year = str(r_year)
            str_month = str(r_month)
            str_day = str(r_day)
            print("email_random là:", email_random)
            print("random_first_name là:", random_first_name)
            print("random_last_name là:", random_last_name)
            print("formatted_dob là:", formatted_dob)
            print("full_phone là:", full_phone)
            print("proxy là:", proxy_dict)
            print("V_Chrome là:", V_Chrome)
            print("----- Bắt đầu gửi request -----") 



            session = requests.Session()
            session.proxies.update(proxy_dict)
            urlAPI1 = "https://www.converse.com/on/demandware.store/Sites-ConverseUS-Site/default/Cms-GetSubscribeModal?auto=10000&actionState=started&contentAssetId=fs-subscription-global-0&isAutoLoad=true&pageID=homepage&format=ajax"

            payload = {}
            session.headers = {
            'accept': 'text/html, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
            'referer': 'https://www.converse.com/',
            'sec-ch-ua': f'"Chromium";v="{V_Chrome}", "Google Chrome";v="{V_Chrome}", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{V_Chrome}.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
            }

            responseAPI1 = session.get(urlAPI1, data=payload, proxies=proxy_dict)

            print ("proxy là:", proxy_dict)
            print("responseAPI1.status_code:", responseAPI1.status_code)
            csrf_token_api1 = responseAPI1.text.split('name="csrf_token" value="')[1].split('"')[0]
            print("csrf_token_api1:", csrf_token_api1)


            urlAPI2 = "https://www.converse.com/on/demandware.store/Sites-ConverseUS-Site/default/Cms-SubscribeHandleFirststep?SubscribeModalData=%7b%22layoutType%22%3anull%2c%22contentAssetId%22%3a%22fs-subscription-global-0%22%2c%22optID%22%3a%22GENERAL_SUB_POPUP%22%2c%22internalID%22%3a%22WelcomeFY21ALL%22%2c%22originalOptID%22%3a%22GENERAL_SUB_POPUP%22%2c%22pageID%22%3a%22homepage%22%2c%22pid%22%3anull%2c%22storeId%22%3anull%2c%22storeCity%22%3anull%2c%22storeState%22%3anull%2c%22storeZip%22%3anull%2c%22contentSquareTrackingKey%22%3anull%2c%22successDuration%22%3a%220%22%2c%22image%22%3anull%2c%22headlineCopy%22%3anull%2c%22subheadlineCopy%22%3anull%2c%22styleList%22%3a%5b%7b%22displayName%22%3a%22Women%27s%20%22%2c%22ID%22%3a%22women%22%7d%2c%7b%22displayName%22%3a%22Men%27s%20%22%2c%22ID%22%3a%22men%22%7d%2c%7b%22displayName%22%3a%22Kids%27%20%22%2c%22ID%22%3a%22kids%22%7d%5d%7d"
            payload = {
                "csrf_token": csrf_token_api1,
                "pageID": "homepage",
                "originalOptID": "GENERAL_SUB_POPUP",
                "dwfrm_subscribe_email": email_random,
                "dwfrm_subscribe_send": "Send",
                "format": "ajax"
            }
            session.headers.update({
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'origin': 'https://www.converse.com', 
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8' 
            })
            responseAPI2 = session.post(urlAPI2, data=payload)
            print("responseAPI2 là:", responseAPI2)
            temp_part = responseAPI2.text.split('name="csrf_token"')[1]
            csrf_token_api2 = temp_part.split('value="')[1].split('"')[0]
            print("csrf_token_api2 là:", csrf_token_api2)


            urlAPI3 = "https://www.converse.com/on/demandware.store/Sites-ConverseUS-Site/default/Cms-SubscribeHandleForm"
            payload_api3 = {
                "csrf_token": csrf_token_api2,
                "pageID": "homepage",
                "originalOptID": "GENERAL_SUB_POPUP",
                "dwfrm_subscribe_email": email_random, 
                "dwfrm_subscribe_firstName": random_first_name,
                "dwfrm_subscribe_lastName": random_last_name,
                "dwfrm_subscribe_country": "us",
                "dwfrm_subscribe_countryDummy": "United States",
                "dwfrm_subscribe_dob": formatted_dob,
                "dwfrm_subscribe_month": str_month,
                "dwfrm_subscribe_day": str_day,
                "dwfrm_subscribe_year": str_year,
                "undefined": "false",
                "dwfrm_subscribe_phone": full_phone,
                "dwfrm_subscribe_promotion": "footer-acquire-new-email-addresses",
                "dwfrm_subscribe_referrer": "",
                "dwfrm_subscribe_send": "Send",
                "format": "ajax"
            }
            self.log.emit(f"🚀 Đang đi lấy code với mã {random_prefix}")

            try:
                responseAPI3 = session.post(urlAPI3, data=payload_api3)
                print("responseAPI3.status_code:", responseAPI3.status_code)
            except Exception as e:
                self.log.emit(f"❌ Lỗi request spam: {e}")
                return 



            if responseAPI3.status_code == 200:
                self.log.emit(f"✅ Spam thành công! Đợi 30s để lấy code...")
                time.sleep(30)

                path_json = get_external_path("config_zoho.json")
                self.apiZoho = zohoapi.ZohoMailAPI(config_path=path_json)
                if not self.apiZoho.refresh_access_token():
                      self.log.emit("❌ Lỗi Token Zoho.")
                      return
                email_list = self.apiZoho.step2_get_emails(email_random)
                if email_list == "TOKEN_EXPIRED":
                    self.apiZoho.refresh_access_token()
                    email_list = self.apiZoho.step2_get_emails(email_random)
                
                if not email_list:
                    self.log.emit("⚠️ Chưa thấy mail, chờ thêm 20s...")
                    time.sleep(20)
                    email_list = self.apiZoho.step2_get_emails(email_random)
                if not email_list:
                    self.log.emit("❌ Không tìm thấy email nào.")
                    return
                for email_random in email_list:
                    print("email_random trong email_list là:", email_random)
                    if not isinstance(email_random, dict): 
                        continue
                    subject = email_random.get("subject", "")
                    if "welcome to converse!" in subject.lower():
                        print(f"\n--- PHÁT HIỆN EMAIL CODE OFF 15% CONVERS: '{subject}' ---")
                        
                        message_id = email_random.get("messageId")
                        print(f"    => Message ID: {message_id}")
                        full_content = self.apiZoho.step3_get_full_content(message_id)
                        print("  full_content là 1 html dài: ")
                        if full_content:
                            print("  Đang chạy bước 4")
                            code = self.apiZoho.step4_code_15converse(full_content)
                            
                            if code:
                                timestamp = time.strftime('%H:%M:%S')
                                print(f"[{timestamp}] KẾT QUẢ CUỐI CÙNG: {code}")
                                try:
                                    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
                                        f.write(f"{code}\n") 
                                    self.log.emit(f"💾 Đã lưu code vào lịch sử: {code}")
                                    print(f" Đã lưu code vào lịch sử: {code} ")
                                except Exception as e:
                                    self.log.emit(f"❌ Lỗi khi lưu file: {e}")
                                return code
                            else:
                                print("    => Lỗi: Không tìm thấy mã code.")
                        else:
                            print("    => Lỗi: Không tải được nội dung chi tiết của email_random này.")
                    else:
                        print(f"    => Bỏ qua email với tiêu đề: '{subject}'")
            else:
                self.log.emit(f"❌ Lỗi Spam API: {responseAPI3.status_code}")
                print(f"❌ Lỗi Spam API: {responseAPI3.status_code}")









        except Exception as e:
            self.log.emit(f"<span style='color: red;'>⚠️ Lỗi hệ thống: {str(e)}</span>")
        finally:
            self.task_completed.emit()

    def run(self):
        self.startCheckBalance()
class Manager(QtWidgets.QMainWindow, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checked_status = []
        
        self.auto_timer = QtCore.QTimer()
        self.auto_timer.setSingleShot(True)
        self.auto_timer.timeout.connect(self.run_check_balance)
        
        self.pushButton_2.clicked.connect(self.start_auto_check)   
        self.pushButton.clicked.connect(self.open_history_code)    
        self.pushButton_4.clicked.connect(self.stop_process)       
        self.pushButton_3.clicked.connect(self.continue_process)   
        
        self.log("✅ UI sẵn sàng")
        
        self.lineEdit.textChanged.connect(lambda: self.updateConfig("lineEdit"))
        self.lineEdit_6.textChanged.connect(lambda: self.updateConfig("lineEdit_6"))
        self.env_file = get_external_path("config.env")
        load_dotenv(self.env_file, encoding='utf-8')
        
        if os.getenv("filedomain"):
            self.lineEdit_6.setText(os.getenv("filedomain"))
        if os.getenv("fileproxy"):
            self.lineEdit.setText(os.getenv("fileproxy"))
        self.is_running_auto = False
        self.check_thread = None 

    def updateConfig(self, text):
        if text == "lineEdit":
            set_key(self.env_file, "fileproxy", self.lineEdit.text())
        if text == "lineEdit_6":
            set_key(self.env_file, "filedomain", self.lineEdit_6.text())

    def start_auto_check(self):
        if not self.is_running_auto:
            self.is_running_auto = True
            self.pushButton_2.setText("Đang chạy tự động...")
            self.pushButton_2.setStyleSheet("background-color: red; color: white; font-weight: bold;")
            self.pushButton_2.setEnabled(False) 
            self.run_check_balance()

    def stop_process(self):
        """Hàm xử lý khi bấm nút DỪNG LẠI"""
        if self.is_running_auto:
            self.is_running_auto = False
            self.auto_timer.stop() 
            self.log("🛑 Đã nhận lệnh DỪNG! Tool sẽ dừng sau khi luồng hiện tại xong (hoặc dừng ngay nếu đang nghỉ).")
            
            self.pushButton_2.setText("Bắt đầu lấy code")
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.setStyleSheet("background-color: #1e90ff; color: white; border-radius: 6px; padding: 6px; font-weight: bold;")
        else:
            self.log("⚠️ Tool đang không chạy.")
    def continue_process(self):
        """Hàm xử lý khi bấm nút TIẾP TỤC"""
        if not self.is_running_auto:
            self.is_running_auto = True
            self.log("▶️ Đang TIẾP TỤC chạy...")
            
            self.pushButton_2.setText("Đang chạy tự động...")
            self.pushButton_2.setStyleSheet("background-color: red; color: white; font-weight: bold;")
            self.pushButton_2.setEnabled(False)
            
            self.run_check_balance()
        else:
            self.log("⚠️ Tool vẫn đang chạy, không cần bấm tiếp tục.")

    def log(self, msg):
        self.txt_log.append(f"[{datetime.now():%H:%M:%S}] {msg}")

    def on_thread_finished(self):
        """Hàm này được gọi khi luồng chạy xong"""
        if self.is_running_auto:
            self.log("⏳ Nghỉ 5 giây trước khi chạy luồng tiếp theo...")
            self.auto_timer.start(5000) 
        else:
            self.log("✅ Tool đã dừng hẳn.")

    def run_check_balance(self):
        if not self.is_running_auto:
            return

        input_fileproxy = self.lineEdit.text().strip()
        proxy_file = input_fileproxy
        
        if not os.path.exists(proxy_file):
            self.log(f"❌ Không thấy file {proxy_file}")
            self.stop_process() # Gọi hàm dừng
            return
            
        try:
            with open(proxy_file, "r", encoding="utf-8") as f:
                list_proxy = [l.strip() for l in f if l.strip()]
            if not list_proxy: 
                self.log("❌ File proxy rỗng")
                self.stop_process()
                return
            proxy_manager = random.choice(list_proxy)
        except Exception as e:
            self.log(f"❌ Lỗi file proxy: {e}")
            self.stop_process()
            return
        
        self.check_thread = MultiThread("Lay_code", proxy=proxy_manager)
        self.check_thread.log.connect(self.log)
        self.check_thread.task_completed.connect(self.on_thread_finished)
        self.check_thread.start()

    def open_history_code(self):
        if os.path.exists(HISTORY_FILE):
            os.startfile(HISTORY_FILE)
            self.log(f"📂 Đã mở file lịch sử: {os.path.basename(HISTORY_FILE)}")
        else:
            self.log("⚠️ File lịch sử chưa tồn tại.")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Manager()
    w.show()
    sys.exit(app.exec_())