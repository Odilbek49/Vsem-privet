import random;

print(type(2323));
print(type('asd'));

list2 = [234, 3423, 564, 668, 'asdsa'];
print(434.65);
list2.append(3242);

print(type(list2));
print(list2);
t= (435,345,345,345);
print(type(t));
print(t);

print(range(6, 453));
d = {'asd': 'asasdasd'};
print(d);
s = {"sdf", "sdf", 'ssf'};
s.add('asdds');
print(s);

fs = frozenset(("apple", "banana", "cherry"));
b = True;
bf = False;
print(fs);

print(b,bf);

print(type(None));


print(int(50.6657));

print(float(54));


print(random.randrange(1,65));

print(random.randint(4,67));
print(random.choice((1,2,3)))

str2 = 'asdgg';

print(str2[1]);
for symbol in str2:
    print(symbol);

print(len(str2));

strHello = '    hello world   ';
print('world' not in strHello);

print(strHello[1:4]);

print(strHello[:5]);

print(strHello[5:]);
print(strHello[-3:-2]);
print(strHello[:]);
print(strHello.upper().lower().strip().lstrip().rstrip().replace('world', 'Sasha').split(' '));


# TODO: принять строку которая должна выглядеть как : Father:Blablabla, Mother:Blablabla, ['Father:Blablabla', ...]  

print('hello, {}'.format(input('enter your name')));

"""
TODO: спросить у пользователя как его зовут, спросить его возраст и вывести текст:
    Тебя зовут "имя", ты родился в "год"
"""