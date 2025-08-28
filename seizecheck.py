import math

def aspect_ratio(width: int, height: int) -> str:
    gcd = math.gcd(width, height)  # наибольший общий делитель
    return f"{width // gcd}:{height // gcd}"

if __name__ == "__main__":
    # пример с Pixel 9 Pro XL
    w, h = 1344, 2992
    atalon = aspect_ratio(w, h)
    print(f"{w}x{h} -> {aspect_ratio(w, h)}")

    # можно протестировать и другие варианты
    sss = ''
    sss1 = 1080
    while sss != atalon:
        sss = aspect_ratio(1080, sss1)
        if sss.startswith("84:"):
            print(f"1080x{sss1} -> {sss}")
        sss1 += 1
        
        # if sss1 == 2000: break
        if str(sss) == str(atalon): break