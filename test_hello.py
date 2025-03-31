from hello import hallo

def test_hallo():
    assert hallo("Alice") == "Hallo, Alice!"
    assert hallo("Bob") == "Hallo, Bob!"
    print("✅ Alle Tests bestanden.")

if __name__ == "__main__":
    test_hallo()
