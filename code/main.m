%用最小二乘法估计s(t)初值和感染系数a（即k0)
clc
clear
load data3.mat
b=0.0046;   % 由Nmub计算所得
%该部分用于计算a和s的初值 采用最小二乘法
s0 = 100:5:30000;  % 估计s初值的取值范围
for n = 1:length(s0)
    s1 = s0(n) + i(1) - i(2) - r(2);  
    m = (s0(n) - s1)./(s0(n).*i(1));
    t = 1:15;
    [T,Y] = ode45('sir',t,[s0(n),i(1),r(1),m,b]);
    for p = 1:15
        SE(p) = (Y(p,2) - i(p)).^2;
    end
    SEE(n) = sum(SE); %此时的残差平方和
end
[v,address] = min(SEE);
s = s0(address); %残差平方和最小的s(t)初值
s1 = s + i(1) - i(2) - r(2);
m = (s - s1)./(s.*i(1)); %残差平方和最小的感染系数a
tspan = 1:70;
[T,Y] = ode45('sir',tspan,[s,i(1),r(1),m,b]);
a=m*Y(1)
figure(1);
t = 1:length(i);
plot(t,i,'rx-');
hold on;
y = Y(1:length(i),2);
y = y';
plot(t,y,'bo-');
legend('真实值','预测值');
xlabel('日期');ylabel('感染人数');
figure(2);
R = Y(1:length(r),3);
R = R';
plot(t,r,'rx-');
hold on;
plot(t,R,'bo-');
legend('真实值','预测值');
xlabel('日期');ylabel('移出人数');
save finaldat

