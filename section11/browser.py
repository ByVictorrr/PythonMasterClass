import webbrowser

#webbrowser.open("https://www.python.org", new=1)

# help(webbrowser)
# for i in range(10):
#     print(1,2,3,sep="\t",end=' ')

chrome = webbrowser.get(using="lynx").open_new("https://github.com/byvictorrr")