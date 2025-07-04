def filter_high_rated_expensive(df):
    # Code Here 
    r = df['rating'] >= 4.5
    q = df['quantity_in_stock'] > 0
    p = df['price'] >= 300
    
    ans = df[r & q & p]
    
    return ans