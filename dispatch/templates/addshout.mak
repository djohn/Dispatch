<%inherit file="base.mak"/>

<div id="content" style="border: 5px inset #98bf21;padding:3px;width:400px;">
	<script>
		dojo.require("dijit.form.Form");
	    dojo.require("dijit.form.TextBox");
	    dojo.require("dijit.form.FilteringSelect");
	    dojo.require("dijit.form.Textarea");
	    dojo.require("dijit.form.Button");
	
		dojo.addOnLoad(function(){
			var myForm = dijit.byId("addShout");
		
			dojo.connect(myForm, "onSubmit", function(e) {
		    	dojo.stopEvent(e);
		    	jform = dojo.toJson(myForm.getValues());
		    	dojo.xhrPost({
					url: "${request.route_url('request', action='add_shout')}",
					handleAs: "json",
					content: myForm.getValues()
		    	});
			});
		});
	</script>
	
    <div dojoType="dijit.form.Form" id="addShout" jsId="addShout" enctype=multipart/form-data charset=utf8 action="" method="">
	<div style="width:100%">
		<!-- text inputs:  dijit.form.TextBox -->
		<strong>Subject: </strong>
		<input type="text" style="width: 100%" name="name" placeholder="New Shout" id="shoutName" dojotype="dijit.form.TextBox">
	</div>
	<div style="width:100%">
		<strong>Owner Id:  </strong>
		<input type="text" style="width: 100%" name="owner" placeholder="ObjectId" id="shoutParent" dojotype="dijit.form.TextBox">
	</div>    
	<div style="width:100%">
		<!-- radio buttons:  dijit.form.FilteringSelect -->
		<strong>Access: </strong>
		<select name="access" id="shoutAccess" style="width: 100%" dojotype="dijit.form.FilteringSelect">
		<option value="public">Public</option>
		<option value="private">Private</option>
		</select>
	</div>	
	<div style="width:100%">
		<strong>Recievership: </strong>
		<textarea id="shoutRecievership" name="recipients" dojoType="dijit.form.Textarea" style="width:100%;"></textarea>
	</div>
	<div style="width:100%">
		<strong>Content: </strong>
		<textarea id="shoutContent" name="content" dojoType="dijit.form.Textarea" style="width:100%;"></textarea>
	</div>
	<div style="width:100%">
		<!-- submit button:  dijit.form.Button -->
		<input type="submit" value="Submit Form" label="Submit Shout" id="submitButton" dojotype="dijit.form.Button">
	</div>
    </div>
</div>