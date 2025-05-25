
%该部分用于计算移出率b（即k2）

load data3
for n = 1:length(r)-1
    r0(n) = (r(n+1) - r(n))./i(n);
end
b = mean(r0)

%b取data3数据结果为0.0046 