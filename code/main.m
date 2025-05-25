%����С���˷�����s(t)��ֵ�͸�Ⱦϵ��a����k0)
clc
clear
load data3.mat
b=0.0046;   % ��Nmub��������
%�ò������ڼ���a��s�ĳ�ֵ ������С���˷�
s0 = 100:5:30000;  % ����s��ֵ��ȡֵ��Χ
for n = 1:length(s0)
    s1 = s0(n) + i(1) - i(2) - r(2);  
    m = (s0(n) - s1)./(s0(n).*i(1));
    t = 1:15;
    [T,Y] = ode45('sir',t,[s0(n),i(1),r(1),m,b]);
    for p = 1:15
        SE(p) = (Y(p,2) - i(p)).^2;
    end
    SEE(n) = sum(SE); %��ʱ�Ĳв�ƽ����
end
[v,address] = min(SEE);
s = s0(address); %�в�ƽ������С��s(t)��ֵ
s1 = s + i(1) - i(2) - r(2);
m = (s - s1)./(s.*i(1)); %�в�ƽ������С�ĸ�Ⱦϵ��a
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
legend('��ʵֵ','Ԥ��ֵ');
xlabel('����');ylabel('��Ⱦ����');
figure(2);
R = Y(1:length(r),3);
R = R';
plot(t,r,'rx-');
hold on;
plot(t,R,'bo-');
legend('��ʵֵ','Ԥ��ֵ');
xlabel('����');ylabel('�Ƴ�����');
save finaldat

