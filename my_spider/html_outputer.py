# coding:utf-8
class HtmlOutputer(object):
    # HTML输出器
    def __init__(self):
        self.datas =[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_out = open('output.html', 'w')

        file_out.write("<html>")
        file_out.write('<head><meta http-equiv="X-UA-Compatible" content="IE=Edge" />')
        file_out.write('<meta charset="utf-8" /></head>')
        file_out.write("<body>")
        file_out.write("<table>")

        for data in self.datas:
            file_out.write("<tr>")
            file_out.write("<td>%s</td>" % data['url'])
            file_out.write("<td>%s</td>" % data['title'])
            file_out.write("<td>%s</td>" % data['summary'])
            file_out.write("</tr>")

        file_out.write("</table>")
        file_out.write("</body>")
        file_out.write("</html>")

