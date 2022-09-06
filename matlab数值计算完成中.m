h = 0.01;
x = 0: h : pi;
y = sin(x);
 
dy_dx1 = diff(y)./diff(x);
dy_dx2 = gradient(y,h);
 
figure;
plot(x,y);
hold on
plot(x(1: end - 1),dy_dx1,'k:');
plot(x,dy_dx2,'r--');
legend('y = sin(x)','导函数曲线（diff）','导函数曲线（gradient）');
xlalel('x');
ylabel('正弦曲线及导函数曲线');