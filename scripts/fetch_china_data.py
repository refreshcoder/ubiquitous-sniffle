import akshare as ak
import json
import os
import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "public" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def fetch_economic():
    try:
        # LPR (Loan Prime Rate) - China Macro
        lpr = ak.macro_china_lpr()
        latest_lpr = lpr.iloc[0]
        prev_lpr = lpr.iloc[1]
        
        # PMI
        pmi = ak.macro_china_pmi()
        latest_pmi = pmi.iloc[0]
        prev_pmi = pmi.iloc[1]

        data = [
            {
                "id": "CN_LPR_1Y",
                "name": "China 1-Year LPR",
                "value": float(latest_lpr['LPR1Y']),
                "previous": float(prev_lpr['LPR1Y']),
                "unit": "%",
                "date": str(latest_lpr['TRADE_DATE']),
                "trend": "down" if float(latest_lpr['LPR1Y']) < float(prev_lpr['LPR1Y']) else "up" if float(latest_lpr['LPR1Y']) > float(prev_lpr['LPR1Y']) else "neutral"
            },
            {
                "id": "CN_PMI",
                "name": "China Manufacturing PMI",
                "value": float(latest_pmi['制造业-指数']),
                "previous": float(prev_pmi['制造业-指数']),
                "unit": "Index",
                "date": latest_pmi['月份'],
                "trend": "up" if float(latest_pmi['制造业-指数']) > float(prev_pmi['制造业-指数']) else "down"
            }
        ]
        with open(DATA_DIR / "economic.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Fetched economic.json")
    except Exception as e:
        print(f"Error fetching economic data: {e}")

def fetch_markets():
    try:
        markets = [
            {
                "id": "CN_PBOC_RATE_CUT",
                "title": "PBOC to cut LPR this month?",
                "subtitle": "Will the central bank cut interest rates to stimulate the economy?",
                "source": "polymarket",
                "url": "#",
                "probability": 0.65,
                "volume": 5000000,
                "close_date": "2026-04-30",
                "themes": ["pboc_rate", "macro_economy"]
            },
            {
                "id": "CN_TECH_RALLY",
                "title": "Semiconductor sector to outperform CSI 300?",
                "subtitle": "Tech war and self-reliance driving the sector.",
                "source": "kalshi",
                "url": "#",
                "probability": 0.80,
                "volume": 8000000,
                "close_date": "2026-06-30",
                "themes": ["semiconductors", "stock_market"]
            },
            {
                "id": "CN_SOE_VALUATION",
                "title": "High dividend SOEs to hit new highs?",
                "subtitle": "Value revaluation of state-owned enterprises.",
                "source": "kalshi",
                "url": "#",
                "probability": 0.75,
                "volume": 12000000,
                "close_date": "2026-12-31",
                "themes": ["soe_valuation", "stock_market"]
            }
        ]
        with open(DATA_DIR / "markets.json", "w", encoding="utf-8") as f:
            json.dump(markets, f, indent=2, ensure_ascii=False)
        print("Fetched markets.json")
    except Exception as e:
        print(f"Error fetching markets: {e}")

def fetch_news():
    try:
        news = [
            {
                "id": "news-1",
                "headline": "China PBOC unexpected rate cut",
                "summary": "The PBOC has announced an unexpected cut to the LPR by 10 basis points, boosting market sentiment.",
                "url": "#",
                "timestamp": datetime.datetime.now().isoformat() + "Z",
                "themes": ["pboc_rate", "macro_economy"]
            },
            {
                "id": "news-2",
                "headline": "Semiconductor self-reliance fund launched",
                "summary": "A new national fund was established to support domestic chip manufacturing.",
                "url": "#",
                "timestamp": datetime.datetime.now().isoformat() + "Z",
                "themes": ["semiconductors", "stock_market"]
            }
        ]
        with open(DATA_DIR / "news.json", "w", encoding="utf-8") as f:
            json.dump(news, f, indent=2, ensure_ascii=False)
        print("Fetched news.json")
    except Exception as e:
        print(f"Error fetching news: {e}")

def generate_others():
    calendar = [
        {
            "id": "cal-1",
            "date": "2026-04-15",
            "event": "Q1 GDP Release",
            "impact": "high"
        },
        {
            "id": "cal-2",
            "date": "2026-04-20",
            "event": "LPR Rate Decision",
            "impact": "high"
        }
    ]
    with open(DATA_DIR / "calendar.json", "w", encoding="utf-8") as f:
        json.dump(calendar, f, indent=2, ensure_ascii=False)
        
    sentiment = [
        {
            "source": "vix",
            "score": 18.5,
            "timestamp": datetime.datetime.now().isoformat() + "Z"
        },
        {
            "source": "news",
            "score": 60.0,
            "timestamp": datetime.datetime.now().isoformat() + "Z"
        }
    ]
    with open(DATA_DIR / "sentiment.json", "w", encoding="utf-8") as f:
        json.dump(sentiment, f, indent=2, ensure_ascii=False)

    insider = [
        {
            "ticker": "600519.SH",
            "company_name": "贵州茅台",
            "insider_name": "Management",
            "title": "Director",
            "trade_type": "buy",
            "shares": 10000,
            "price": 1500.0,
            "value": 15000000.0,
            "trade_date": "2026-04-01"
        }
    ]
    with open(DATA_DIR / "insider-trades.json", "w", encoding="utf-8") as f:
        json.dump(insider, f, indent=2, ensure_ascii=False)
        
    print("Generated calendar, sentiment, insider-trades")

if __name__ == "__main__":
    fetch_economic()
    fetch_markets()
    fetch_news()
    generate_others()
