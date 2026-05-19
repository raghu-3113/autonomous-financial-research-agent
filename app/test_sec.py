from tools.sec_tool import get_sec_filings

results = get_sec_filings("AAPL")

print("\nSEC RESULTS:\n")

for r in results:

    print("\n-------------------\n")

    print(r)