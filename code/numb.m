
%�ò������ڼ����Ƴ���b����k2��

load data3
for n = 1:length(r)-1
    r0(n) = (r(n+1) - r(n))./i(n);
end
b = mean(r0)

%bȡdata3���ݽ��Ϊ0.0046 