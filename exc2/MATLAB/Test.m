close all; clear; clc;

t = 1:0.01:10;
h = 3 .* pi .* exp(- 5.*sin(2.*pi.*1.*t));
plot(t,h)