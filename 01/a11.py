def numinput(uzenet, db):
    m_num = 0
    for i in range(db):
        m_str = input(uzenet)
        try:
            m_num = int(m_str)
        except:
            continue
        break
    return m_num

m = numinput("hány macskád van? ",3)
if m > 5:
    print("az sok: " + str(m))
elif m >0:
    print("nem olyan sok " + str(m))
else:
    print("nincs is macskád")
