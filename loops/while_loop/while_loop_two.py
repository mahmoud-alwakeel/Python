myFriends = ["ab", "bc", "cd", "de", "ef", "fg", "gh", "hi", "ij", "jk"]
print(len(myFriends))

a = 0

while a < len(myFriends):
    print(f"number {str((a+1)).zfill(2)}: {myFriends[a]}")
    a += 1
print("all friends are printed")