data = SN280ECorrectedsummary;
% data = SN280EUnitysummary;
% getFile
% data = DataTable

raw_xx = ((data.GYRXs(11)-data.GYRXs(12))/2);
raw_xy = ((data.GYRYs(11)-data.GYRYs(12))/2);
raw_xz = ((data.GYRZs(11)-data.GYRZs(12))/2);
raw_yx = ((data.GYRXs(5)-data.GYRXs(6))/2);
raw_yy = ((data.GYRYs(5)-data.GYRYs(6))/2);
raw_yz = ((data.GYRZs(5)-data.GYRZs(6))/2);
raw_zx = ((data.GYRXs(1)-data.GYRXs(2))/2);
raw_zy = ((data.GYRYs(1)-data.GYRYs(2))/2);
raw_zz = ((data.GYRZs(1)-data.GYRZs(2))/2);

rawA_xx = ((data.ACCXmg(4)-data.ACCXmg(3))/2);
rawA_xy = ((data.ACCYmg(4)-data.ACCYmg(3))/2);
rawA_xz = ((data.ACCZmg(4)-data.ACCZmg(3))/2);
rawA_yx = ((data.ACCXmg(8)-data.ACCXmg(10))/2);
rawA_yy = ((data.ACCYmg(8)-data.ACCYmg(10))/2);
rawA_yz = ((data.ACCZmg(8)-data.ACCZmg(10))/2);
rawA_zx = ((data.ACCXmg(9)-data.ACCXmg(7))/2);
rawA_zy = ((data.ACCYmg(9)-data.ACCYmg(7))/2);
rawA_zz = ((data.ACCZmg(9)-data.ACCZmg(7))/2);


% raw_xx = ((data.XGYR0(11)-data.XGYR0(12))/2)/100;
% raw_xy = ((data.YGYR0(11)-data.YGYR0(12))/2)/100;
% raw_xz = ((data.ZGYR0(11)-data.ZGYR0(12))/2)/100;
% raw_yx = ((data.XGYR0(5)-data.XGYR0(6))/2)/100;
% raw_yy = ((data.YGYR0(5)-data.YGYR0(6))/2)/100;
% raw_yz = ((data.ZGYR0(5)-data.ZGYR0(6))/2)/100;
% raw_zx = ((data.XGYR0(1)-data.XGYR0(2))/2)/100;
% raw_zy = ((data.YGYR0(1)-data.YGYR0(2))/2)/100;
% raw_zz = ((data.ZGYR0(1)-data.ZGYR0(2))/2)/100;
% 
% rawA_xx = ((data.XACC0(4)-data.XACC0(3))/2);
% rawA_xy = ((data.YACC0(4)-data.YACC0(3))/2);
% rawA_xz = ((data.ZACC0(4)-data.ZACC0(3))/2);
% rawA_yx = ((data.XACC0(8)-data.XACC0(10))/2);
% rawA_yy = ((data.YACC0(8)-data.YACC0(10))/2);
% rawA_yz = ((data.ZACC0(8)-data.ZACC0(10))/2);
% rawA_zx = ((data.XACC0(9)-data.XACC0(7))/2);
% rawA_zy = ((data.YACC0(9)-data.YACC0(7))/2);
% rawA_zz = ((data.ZACC0(9)-data.ZACC0(7))/2);

delta = [
    raw_xx raw_xy raw_xz;
    raw_yx raw_yy raw_yz;
    raw_zx raw_zy raw_zz
    ];

deltaA = [
    rawA_xx rawA_xy rawA_xz;
    rawA_yx rawA_yy rawA_yz;
    rawA_zx rawA_zy rawA_zz
    ];


M = [
    9.999980E-01, 2.031664E-04, 2.044291E-03;
    7.175626E-05, 1.000000E+00, -8.585742E-04;
    -2.445849E-03, 1.727035E-03, 9.999960E-01
    ];


% M1 = Mi(1,:);
% M2 = Mi(2,:);
% M3 = Mi(3,:);

% clc
% newx = dotter(M1, raw_xx, raw_xy, raw_xz);
% newy = dotter(M2, raw_xx, raw_xy, raw_xz);
% newz = dotter(M3, raw_xx, raw_xy, raw_xz);


[oldx, oldy, oldz] = oldway(M, raw_xx, raw_xy, raw_xz);





%% Accelerometer Misalignment
mult = 0.02
a_m_yx = atand(rawA_xy / 1000);
a_m_zx = atand(rawA_xz / 1000);
a_m_xy = atand(rawA_yx / 1000);
a_m_zy = atand(rawA_yz / 1000);
a_m_xz = atand(rawA_zx / 1000);
a_m_yz = atand(rawA_zy / 1000);
accel_m_yx = ((a_m_yx - a_m_xy) / mult);
accel_m_zx = ((a_m_zx - a_m_xz) / mult);
accel_m_xy = ((a_m_xy - a_m_yx) / mult);
accel_m_zy = ((a_m_zy - a_m_yz) / mult);
accel_m_xz = ((a_m_xz - a_m_zx) / mult);
accel_m_yz = ((a_m_yz - a_m_zy) / mult);

Ma = [0 accel_m_yx accel_m_zx;
     accel_m_xy 0 accel_m_zy;
     accel_m_xz accel_m_yz 0]

% Plot figure
figure;
hold on;
title('Accelerometer Misalignment');
% Set limits and labels for the figure
% xlim([-0.1,1.1]); ylim([-0.1,1.1]); zlim([-0.1,1.1]);
xlabel('X'); ylabel('Y'); zlabel('Z');
% Set the default orientation for the plot view
az = 139;
el = 30;
view(az, el);

% Plot the ideal and misaligned axes
quiver3(0,0,0,1,0,0,1,'LineWidth',2,'color','k');
quiver3(0,0,0,0,1,0,1,'LineWidth',2,'color','k');
quiver3(0,0,0,0,0,1,1,'LineWidth',2,'color','k');
q1=quiver3(0,0,0,cosd(accel_m_xy)*cosd(accel_m_xz),sind(accel_m_xy),sind(accel_m_xz),1,'LineWidth',1,'color','r');
q2=quiver3(0,0,0,sind(accel_m_yx),cosd(accel_m_yx)*cosd(accel_m_yz),sind(accel_m_yz),1,'LineWidth',1,'color','g');
q3=quiver3(0,0,0,sind(accel_m_zx),sind(accel_m_zy),cosd(accel_m_zx)*cosd(accel_m_zy),1,'LineWidth',1,'color','b');


%% Gyroscope Misalignment
mult = 0.02
a_m_yx = atand(raw_xy / 288);
a_m_zx = atand(raw_xz / 288);
a_m_xy = atand(raw_yx / 288);
a_m_zy = atand(raw_yz / 288);
a_m_xz = atand(raw_zx / 288);
a_m_yz = atand(raw_zy / 288);
accel_m_yx = ((a_m_yx - a_m_xy) / mult);
accel_m_zx = ((a_m_zx - a_m_xz) / mult);
accel_m_xy = ((a_m_xy - a_m_yx) / mult);
accel_m_zy = ((a_m_zy - a_m_yz) / mult);
accel_m_xz = ((a_m_xz - a_m_zx) / mult);
accel_m_yz = ((a_m_yz - a_m_zy) / mult);

Mg = [0 accel_m_yx accel_m_zx;
     accel_m_xy 0 accel_m_zy;
     accel_m_xz accel_m_yz 0]

% Plot figure
figure;
hold on;
title('Gyroscope Misalignment');
% Set limits and labels for the figure
% xlim([-0.1,1.1]); ylim([-0.1,1.1]); zlim([-0.1,1.1]);
xlabel('X'); ylabel('Y'); zlabel('Z');
% Set the default orientation for the plot view
az = 139;
el = 30;
view(az, el);

% Plot the ideal and misaligned axes
quiver3(0,0,0,1,0,0,1,'LineWidth',2,'color','k');
quiver3(0,0,0,0,1,0,1,'LineWidth',2,'color','k');
quiver3(0,0,0,0,0,1,1,'LineWidth',2,'color','k');
q1=quiver3(0,0,0,cosd(accel_m_xy)*cosd(accel_m_xz),sind(accel_m_xy),sind(accel_m_xz),1,'LineWidth',1,'color','r');
q2=quiver3(0,0,0,sind(accel_m_yx),cosd(accel_m_yx)*cosd(accel_m_yz),sind(accel_m_yz),1,'LineWidth',1,'color','g');
q3=quiver3(0,0,0,sind(accel_m_zx),sind(accel_m_zy),cosd(accel_m_zx)*cosd(accel_m_zy),1,'LineWidth',1,'color','b');