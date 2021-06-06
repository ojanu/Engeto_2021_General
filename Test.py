import os

os.mkdir('Test')
print(os.listdir())

os.mkdir("Test/TestDir1")
os.mkdir("Test/TestDir2")
os.mkdir("Test/TestDir3")

f = open('Test/TestDir1/config.txt', 'w')
f.close()
f = open('Test/TestDir1/tasks.txt', 'w')
f.close()
f = open('Test/TestDir1/test.txt', 'w')
f.close()

print(os.listdir())
print(os.listdir(path='Test/TestDir1'))

os.rename('Test/TestDir1/tasks.txt', 'Test/TestDir1/todo.txt')
os.rename('Test/TestDir1/config.txt', 'Test/TestDir2/config.txt')
os.rename('Test/TestDir1/test.txt', 'Test/TestDir3/review.txt')
print(os.listdir())
print(os.listdir(path='Test/TestDir1'))
print(os.listdir(path='Test/TestDir2'))
print(os.listdir(path='Test/TestDir3'))

os.rename('Test/TestDir1/todo.txt', 'Test/TestDir1/tasks.txt')
os.rename('Test/TestDir2/config.txt', 'Test/TestDir1/config.txt')
os.rename('Test/TestDir3/review.txt', 'Test/TestDir1/test.txt')
print(os.listdir())
print(os.listdir(path='Test/TestDir1'))
print(os.listdir(path='Test/TestDir2'))
print(os.listdir(path='Test/TestDir3'))

os.remove('Test/TestDir1/test.txt')
print(os.listdir())
print(os.listdir(path='Test/TestDir1'))
print(os.listdir(path='Test/TestDir2'))
print(os.listdir(path='Test/TestDir3'))

os.rmdir('Test/TestDir2')
print(os.listdir(path='Test'))
print(os.listdir(path='Test/TestDir1'))
print(os.listdir(path='Test/TestDir2'))
print(os.listdir(path='Test/TestDir3'))

