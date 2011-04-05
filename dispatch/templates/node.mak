<%inherit file="base.mak"/>

<ul>
    % for node in nodes:
	<li>
	    Node: ${node['name']}</br>
	    ID: ${node['_id']}
	</li>
    % endfor
</ul>