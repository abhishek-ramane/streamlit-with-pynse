from jugaad_data.nse import NSELive

n = NSELive()
quotes = n.stock_quote_fno("HDFC")

for quote in quotes['stocks']:
    print("{}\t{}".format(quote['metadata']['identifier'], quote['metadata']['lastPrice']))
