---
title: Exámenes de convocatorias anteriores
---
<div class="alert">
    <a href="{{data.root}}" target="_blank">Convocatorias</a>
</div>

{% set o = data['A1'] %}

<table>
<thead>
<tr>
  <th colspan="6">
    <a href="{{o.url}}">{{o.codigo}} {{o.titulo}}</a>
  </th>
</tr>
</tr>
  <th colspan="2" rowspan="2">Convocatoria</th>
  <th colspan="4">Ejercicios</th>
</tr>
</tr>
  <th>1</th>
  <th>2</th>
  <th>3</th>
  <th>4</th>
</tr>
</thead>
<tbody>
{% for c in o.convocatorias %}
<tr>
  <th><a href="{{c.url}}">{{c.year}} {{c.ingreso}}</a></th>
</tr>
{% endfor %}
</tbody>
</table>
