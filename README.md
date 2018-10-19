# buffer-python
Buffer Vector Creation in Python.
 
Buffer analysis is one of the several important spatial analysis functions of geographical information system ( GIS). Buffer creation can be divided into three types: for points, lines and polygons, the buffer creation for lines is the key and basis. A new kind of effective buffer radius-rotation vector creation algorithm based on buffer vector creation algorithm of circular arc was presented.

## introduction
线状缓冲区的建立是以线状目标为参考轴线, 离开轴线向两侧沿法线方向平移一定距离,并在线端点(如半圆弧)连接,所得到的点组成的封闭区域即为线状目标的缓冲区。 由于线状目标在 GIS 中是以坐标的形式存储的, 因此生成线状目标缓冲区的过程是对线状目标上的坐标点逐点求得其缓冲点的过程。将线状目标中点的坐标根据存储位置的前后视为有方向差异，则线状目标即为有方向的。在计算目标点的缓冲区点时，约定总是计算目标点的左侧缓冲区点，当遍历一次目标点之后，再反方向遍历目标点，在计算每个目标点的左侧缓冲区点（原方向的右侧缓冲区点），按计算顺序将缓冲区点连接，最终形成缓冲区。

## definition
  * 有序坐标点构成的曲线成为轴线
  * 轴线上两条相邻的线段的交点称为拐点
  * 轴线上顺序三点，用右手螺线法则，若拇指朝上，则中间点左凹右凸；若拇指朝下，则中间点左凸右凹。
  * 平面直角坐标系中某一直线与坐标主轴（X轴）之间的夹角，从主轴起算，逆时针方向自0~360度为方位角
  * 轴线中的两个拐点构成的向量，在方向上总是指向轴线方向上的后一个拐点

## bump and pits
根据定义，通过右手螺旋法则确定一个点的凹凸性，由于在本例中只考虑左侧缓冲区点的计算，故若拇指朝上，则中间点为凹点；若拇指朝下，则中间点为凸点。

在具体计算时，为了确定中间点在确定方向上的凹凸性，可运用向量叉积的计算结果进行判定,若叉积<0,则为凹点；反之，则为凸点。这里强调确定方向是因为一个点若在一个方向上是凸点，则在反方向上必为凹点，凹凸点的左侧缓冲区点的计算算法不同，所以要严格的加以区分。此外，向量叉积的计算结果与两个向量的前后位置有直接关系，若a*b<0,则b*a>0。故在计算包含中心点的两个向量的叉积时，在此例中约定按照轴线方向，定义两向量的叉积为：前向量*后向量。

判定点的凹凸性后，凹点使用角平分线法确定左缓冲区点，凸点使用半径旋转法确定左缓冲区点。

## angular bisectrix algorithm
图
> **alpha角为一个向量的方位角**

> **delta角为两个向量的夹角（0 <= delta <= 180），分局向量内积的计算法则定义，实则直线夹角的补角**

从图中的图形关系得
> ***beta=alpha+（180-delta）/2***，**beta为角平分线的方向角** (角度顺时针方向旋转即为“+”，逆时针方向为“-”)

>***x1=x0+R/sin(180-delta)/2 * cos(deta)***

>***y1=y0+R/sin(180-delta)/2 * sin(deta)***

据此，得到凹点的唯一缓冲点

## buffer radius-rotation vector creation algorithm


