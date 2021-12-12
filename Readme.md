## Advent of Code 2021 Solutions

Here I'll be updating my [**Advent Of Code 2021**](https://adventofcode.com/) event solutions. I'm solving each daily challenge using an ipython Noteebok, saved the first days, wich I naively tried to solve using C. 

**Topics covered so far:**

- Christmas 
- Elves 
- Submarines 
- Pulps 
- Wales 
- Caves
- Chunks
- Faulty Navigation Systems

<style>
.calendar .calendar-color-w4 { color:#0091cc; }
.calendar .calendar-color-w6 { color:#0079b5; }
.calendar .calendar-color-s { color:#ffffff; }
.calendar .calendar-color-g { color:#a47a4d; }
.calendar .calendar-color-w5 { color:#0085c0; }
.calendar .calendar-color-w1 { color:#00c8ff; }
.calendar .calendar-color-w9 { color:#005a98; }
.calendar .calendar-color-r { color:#ff0000; }
.calendar .calendar-color-w10 { color:#005291; }
.calendar .calendar-color-o { color:#c74c30; }
.calendar .calendar-color-w7 { color:#006daa; }
.calendar .calendar-color-w8 { color:#00619f; }
.calendar .calendar-color-w12 { color:#004282; }
.calendar .calendar-color-w3 { color:#00a2db; }
.calendar .calendar-color-w11 { color:#004a8a; }
.calendar .calendar-color-w2 { color:#00b5ed; }
</style>

<pre class="calendar">
<a aria-label="Day 1, two stars" class="calendar-day1 calendar-verycomplete"><span class="calendar-color-w1">~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>  <span class="calendar-day"> 1</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 2, two stars" class="calendar-day2 calendar-verycomplete"><span class="calendar-color-w2"> .    .    .   .       '  '.    </span> <span class="calendar-color-s">.</span> <span class="calendar-color-w2">.      </span> <span class="calendar-color-g">..''''</span>  <span class="calendar-day"> 2</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 3, two stars" class="calendar-day3 calendar-verycomplete"><span class="calendar-color-w3">   ~     . .                '. </span> <span class="calendar-color-s">.</span> <span class="calendar-color-w3">. ~   .</span> <span class="calendar-color-g">:</span>        <span class="calendar-day"> 3</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 4, two stars" class="calendar-day4 calendar-verycomplete"><span class="calendar-color-w4">    .. . .    .   .          . </span> <span class="calendar-color-s">.'</span> <span class="calendar-color-w4">  </span> <span class="calendar-color-g">....'</span>        <span class="calendar-day"> 4</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 5, two stars" class="calendar-day5 calendar-verycomplete"><span class="calendar-color-w5">           .        ...      </span> <span class="calendar-color-o">.</span><span class="calendar-color-r">.</span><span class="calendar-color-s">|\</span><span class="calendar-color-r">.</span><span class="calendar-color-o">.</span><span class="calendar-color-g">''</span>             <span class="calendar-day"> 5</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 6, two stars" class="calendar-day6 calendar-verycomplete"><span class="calendar-color-w6"> ~               .         .</span> <span class="calendar-color-g">:</span>                     <span class="calendar-day"> 6</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 7, two stars" class="calendar-day7 calendar-verycomplete"><span class="calendar-color-w7">           . '  .  .      </span> <span class="calendar-color-g">:'</span>                      <span class="calendar-day"> 7</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 8, two stars" class="calendar-day8 calendar-verycomplete"><span class="calendar-color-w8">.    . '   .          .   </span>  <span class="calendar-color-g">'''''.....</span>  <span class="calendar-color-g">..</span><span class="calendar-color-o">.</span><span class="calendar-color-r">.</span>       <span class="calendar-day"> 8</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 9, two stars" class="calendar-day9 calendar-verycomplete"><span class="calendar-color-w9"> .                   . . </span> <span class="calendar-color-g">:'..</span>  <span class="calendar-color-g">..</span>    <span class="calendar-color-g">''</span>    <span class="calendar-color-r">':</span>     <span class="calendar-day"> 9</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 10, two stars"  class="calendar-day10 calendar-verycomplete"><span class="calendar-color-w10">    '   ' .   .       .  </span> <span class="calendar-color-g">:</span>   <span class="calendar-color-g">''</span>  <span class="calendar-color-g">''''..</span>     <span class="calendar-color-o">'</span><span class="calendar-color-g">.</span>    <span class="calendar-day">10</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 11, two stars"class="calendar-day11 calendar-verycomplete"><span class="calendar-color-w11">      '      .           </span> <span class="calendar-color-g">:</span>             <span class="calendar-color-g">'..'.</span> <span class="calendar-color-g">:</span>    <span class="calendar-day">11</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<a aria-label="Day 12, two stars" class="calendar-day12 calendar-verycomplete"><span class="calendar-color-w12">        '    .          </span>         :'''..   <span class="calendar-color-g">..'</span> <span class="calendar-color-g">:</span>    <span class="calendar-day">12</span> <span class="calendar-mark-complete">*</span><span class="calendar-mark-verycomplete">*</span></a>
<span aria-hidden="true" class="calendar-day13">     ..      .. '                      '<span class="calendar-color-g">''</span> <span class="calendar-color-g">...:</span>    <span class="calendar-day">13</span><span id="calendar-countdown"></span>
</pre>
