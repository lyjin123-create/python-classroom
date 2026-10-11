import requests

# [부록 예제] 오픈 API 활용 실시간 환율 조회

def check_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        rates = data["rates"]
        usd_to_krw = rates["KRW"]
        usd_to_jpy = rates["JPY"]
        
        print("🌍 [글로벌 실시간 환율 정보]")
        print("-" * 30)
        print(f"1 달러(USD) = {usd_to_krw:,.2f} 원(KRW)")
        print(f"1 달러(USD) = {usd_to_jpy:,.2f} 엔(JPY)")
        print(f"100 엔(JPY) = {(usd_to_krw / usd_to_jpy) * 100:,.2f} 원(KRW)")
        print("-" * 30)
    except Exception as e:
        print(f"⚠️ 환율 데이터를 불러올 수 없습니다: {e}")

if __name__ == "__main__":
    check_rates()
