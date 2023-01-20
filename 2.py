from flask import Flask, render_template, request

app = Flask(__name__)
word = None
@app.route('/', methods=['GET', 'POST'])
def test():
   global word
   word = request.form.get("word")
   if word != None:
       if str(word) == str(word)[::-1]:
           res = True
       else:
           res = False

   else:
       word, res = '', ''
   return render_template("index.html", res=res, word = word)


if __name__ == '__main__':
   app.run()