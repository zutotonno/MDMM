<?xml version = "1.1" encoding="UTF-8" standalone="yes"?>
<CmplSolutions version="1.0">
   <general>
       <instanceName>inst_10_50_100_50_75_25_45$_01_1.cmpl</instanceName>
       <nrOfVariables>1000</nrOfVariables>
       <nrOfConstraints>305</nrOfConstraints>
       <objectiveName>cost</objectiveName>
       <objectiveSense>min</objectiveSense>
       <nrOfSolutions>1</nrOfSolutions>
       <solverName>GLPK</solverName>
       <variablesDisplayOptions>nonZeroVariables (all)</variablesDisplayOptions>
       <constraintsDisplayOptions>nonZeroConstraints (all)</constraintsDisplayOptions>
   </general>
   <solution idx="0" status="optimal" value="1407">
       <variables>
           <variable idx="62" name="y[1,4,2,1]" type="I" activity="1" lowerBound="0" upperBound="1" marginal="NaN"/>
           <variable idx="374" name="y[2,9,8,1]" type="I" activity="1" lowerBound="0" upperBound="1" marginal="NaN"/>
           <variable idx="480" name="y[3,5,1,1]" type="I" activity="1" lowerBound="0" upperBound="1" marginal="NaN"/>
           <variable idx="678" name="y[4,4,10,1]" type="I" activity="1" lowerBound="0" upperBound="1" marginal="NaN"/>
           <variable idx="982" name="y[5,10,2,1]" type="I" activity="1" lowerBound="0" upperBound="1" marginal="NaN"/>
       </variables>
       <linearConstraints> 
           <constraint idx="2" name="bilancio[1,3]" type="E" activity="1" lowerBound="1" upperBound="1" marginal="NaN"/>
           <constraint idx="5" name="bilancio[2,1]" type="E" activity="1" lowerBound="1" upperBound="1" marginal="NaN"/>
           <constraint idx="9" name="bilancio[2,5]" type="E" activity="1" lowerBound="1" upperBound="1" marginal="NaN"/>
           <constraint idx="15" name="bilancio[4,1]" type="E" activity="-1" lowerBound="-1" upperBound="-1" marginal="NaN"/>
           <constraint idx="18" name="bilancio[4,4]" type="E" activity="-1" lowerBound="-1" upperBound="-1" marginal="NaN"/>
           <constraint idx="22" name="bilancio[5,3]" type="E" activity="-1" lowerBound="-1" upperBound="-1" marginal="NaN"/>
           <constraint idx="36" name="bilancio[8,2]" type="E" activity="1" lowerBound="1" upperBound="1" marginal="NaN"/>
           <constraint idx="41" name="bilancio[9,2]" type="E" activity="-1" lowerBound="-1" upperBound="-1" marginal="NaN"/>
           <constraint idx="48" name="bilancio[10,4]" type="E" activity="1" lowerBound="1" upperBound="1" marginal="NaN"/>
           <constraint idx="49" name="bilancio[10,5]" type="E" activity="-1" lowerBound="-1" upperBound="-1" marginal="NaN"/>
           <constraint idx="112" name="capacity[4,2,1]" type="L" activity="94" lowerBound="-INF" upperBound="295" marginal="NaN"/>
           <constraint idx="128" name="capacity[4,10,1]" type="L" activity="79" lowerBound="-INF" upperBound="267" marginal="NaN"/>
           <constraint idx="130" name="capacity[5,1,1]" type="L" activity="54" lowerBound="-INF" upperBound="168" marginal="NaN"/>
           <constraint idx="224" name="capacity[9,8,1]" type="L" activity="70" lowerBound="-INF" upperBound="127" marginal="NaN"/>
           <constraint idx="232" name="capacity[10,2,1]" type="L" activity="52" lowerBound="-INF" upperBound="261" marginal="NaN"/>
           <constraint idx="250" name="lunghezza[1]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="251" name="lunghezza[2]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="252" name="lunghezza[3]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="253" name="lunghezza[4]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="254" name="lunghezza[5]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="258" name="unico[1,4]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="273" name="unico[2,9]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="279" name="unico[3,5]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="288" name="unico[4,4]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
           <constraint idx="304" name="unico[5,10]" type="L" activity="1" lowerBound="-INF" upperBound="1" marginal="NaN"/>
       </linearConstraints>
   </solution>
</CmplSolutions>
