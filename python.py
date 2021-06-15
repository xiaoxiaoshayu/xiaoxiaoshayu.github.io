import random as ran

with open("word1s.txt","r+") as file:
    wordss=file.read()
    words=eval(wordss)

    print("""
                       【《 欢迎使用单词速背系统 》】
                             
              英译汉请输入:Q   汉译英请输入:W   添加单词请按:E
                 
              模拟练习请按:R   结束程序请按:T   查看所有单词:Y
          """)
    print("--------------- start ----------------")
    key=input("请输入选择的按键：")
    while(1):
          if (key=='W'or key=='w'):
              
                            kiocd= {v : k for k, v in words.items()}
                            n=input("请输入需要查询单词的中文：")
                            if n in kiocd:
                                  print(kiocd[n])
                            else:
                                  print('知识有限，敬请期待！！！')
                            print("--------------- 新的开始 ------------------")       
                            key=input("\n请继续选择需要的按键: ")
                            
                            
          elif (key=='Q'or key=='q'):
              
                            n=input("请输入需要查询单词的英文：")
                            if n in words:
                                  print(words[n])
                            else:
                                  print('知识有限，敬请期待！！！')
                            print("--------------- 新的开始 ------------------")      
                            key=input("\n请继续选择需要的按键: ")
                            
                            
          elif (key=='R'or key=='r'):
              
                            i=0
                            z=0
                            while(i<5):
                                  word1=ran.choice(list(words))
                                  word2=words[word1]
                                  print(word1)
                                  user=input("请输入这个单词的释义：")
                                  if user == word2:
                                        print('恭喜您，答对了') 
                                        z=z+1              
                                  else:
                                        print('很遗憾，答错了，请再接再厉哦！！！')
                                        print('正确答案是:{}'.format(word2))      
                                  i=i+1

                            while(i>=5 and i<10):
                                  word1=ran.choice(list(words))
                                  word2=words[word1]
                                  print(word2)
                                  user=input("请输入这个单词的释义：")
                                  if user == word1:
                                        print('恭喜您，答对了') 
                                        z=z+1              
                                  else:
                                        print('很遗憾，答错了，请再接再厉哦！！！')
                                        print('正确答案是:{}'.format(word2))      
                                  i=i+1
                            print('恭喜您，本次模拟结束，本次您的正确率为:{:.2%}'.format(z/10))
                            key=input("\n任意按键继续下一组测试：")
                            print("------------- 下一组测试 ---------------")
                                               
          elif (key=='E'or key=='e'):
                
                                  print("")
                                  print("使用添加后需让程序结束再关闭，否则会有异常，造成数据丢失！！！")
                                  print("")
                                  new_key=input('请输入这个新单词的英文：')
                                  new_value=input('请输入这个新单词的意思：')
                                  words[new_key]= new_value
                                  file.seek(0)
                                  file.truncate()
                                  file.write(str(words))
                                  print("--------------- 新的开始 ------------------")     
                                  key=input("\n请继续选择需要的按键: ")
                                        
          elif(key=='T'or key=='t'):
              
                            print("程序已经退出，欢迎您的下次使用！！！")
                            break
                         
