%Quiz 6

clear all
clc

inputvalues = input('Input the x and y values in the form of a matrix, Column 1 contains x values, Column 2 contains y values: ');
order = input('Input the order of the curve fit: ');

sizev = size(inputvalues);
ndata = sizev(1);

%find B
bvalue=[];
for b=0:order
    datahold=0;
    for n=1:ndata
        datahold =datahold+ inputvalues(n,2) * (inputvalues(n,1))^b;
    end
    bvalue(b+1,1)=datahold;
end
%create the matrix
xvaluem=[];
for b=0:order
    for apos=0:order
        datahold=0;
        for n=1:ndata
            datahold = datahold + (inputvalues(n,1))^(b+apos);
        end
        xvaluem(b+1,apos+1)=datahold;
    end
end
%solve the matrix
avalues = inv(xvaluem) * bvalue;


eq = 'F(x) =';
eq = strcat(eq,[' (', num2str(avalues(1)),')']);
for count=1:order
    if count ==1
        eq = strcat(eq,[' + (',num2str(avalues(count+1)),')x']);
    else
        eq = strcat(eq,[' + (',num2str(avalues(count+1)),')x^',num2str(count)]);
    end
end

%display values
disp('Coefficients are: ');
disp(avalues);
disp('Polynomial fit ressembles: ');
disp(eq);
