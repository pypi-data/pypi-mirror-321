# index.py

from lib import pinyin, detailedPinyin, all

def main():
    # Example usage of the functions
    char = '阿'
    print(f"Pinyin for '{char}': {pinyin(char)}")
    print(f"Detailed Pinyin for '{char}': {detailedPinyin(char)}")
    # print(f"All entries: {all()}")

if __name__ == "__main__":
    main()
