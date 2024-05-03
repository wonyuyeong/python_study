from lxml import etree

# Data
members = ["소원", "예린", "은하", "유주", "신비", "엄지"]
albums = [["EP 1집", "Season of Glass"], ["EP 2집", "Flower Bud"],
          ["EP 3집", "Snowflake"], ["정규 1집","LOL"],
          ["EP 4집", "THE AWAKENING"]]

# Create XML
root = etree.Element("girlgroup")

# name
x_name = etree.Element("name")
x_name.text = "여자친구"
x_name.set("alias", "GFRIEND")

x_members = etree.Element("members")
for i in members :
    x_member = etree.SubElement(x_members, "member")
    x_member.text = i

x_albums = etree.Element("albums")
for i in albums:
    x_album = etree.SubElement(x_albums, "album")
    x_album.text = i[1]
    # 속성
    x_album.set("order", i[0])
    

root.append(x_name)
root.append(x_members)
root.append(x_albums)

# 출력
x_output = etree.tostring(root, pretty_print=True, encoding="utf-8")
x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
print(x_header+x_output.decode("utf-8"))

# xml 파일로 만들기
x_output = etree.tostring(root, pretty_print=True, encoding="utf-8")
x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
f = open("day05/data/sample.xml", "w", encoding="utf-8")
f.write(x_header+x_output.decode("utf-8"))
f.close()
