import csv

def articleJSON(row):
    final_output = ''
    final_output += "<html>\n  <head>\n    "
    final_output += "<title>" + row[3] + "</title>\n"
    final_output += '    <script type="application/ld+json">'
    final_output += '\n    {\n      '
    final_output += '"@context": "https://schema.org",\n      "@type": "'
    final_output += row[2] + '",\n      "headline": "'
    final_output += row[3] + '",\n      "image": [\n        "'
    final_output += row[4] + '",\n        "'
    final_output += row[5] + '",\n        "'
    final_output += row[6] + '"\n       ],\n      "datePublished": "'
    final_output += row[7] + '",\n      "dateModified": "'
    final_output += row[8] + '"\n    }\n'
    final_output += "    </script>\n  </head>\n  <body>\n  </body>\n</html>"
    return final_output

    
with open('StructuredData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count == 0):
            line_count = line_count + 1
            continue
        else :
            if (row[1] == "Article") :
                text_file = open("output.txt", "wt")
                text_file.write(row[0]+" " + row[3]+"\n"+articleJSON(row))
                text_file.close()
