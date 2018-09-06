const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

exports.createNewData = functions.firestore.document('zzchecking/{stationName}').onWrite((change, context) => {
	const newValue = change.after.data();
	const locationValue = newValue.Station_Name;
	const dateValue = newValue.Date;
	const timeValue = newValue.Time;
	const waterLevel = newValue.Info.Water_Level;
	const alertLevel = newValue.Alert_System.Alert_Level;
	const warningLevel = newValue.Alert_System.Warning_Level;
	const dangerLevel = newValue.Alert_System.Danger_Level;
	
	var body, title;
	
	if (waterLevel >= dangerLevel) {
		title = "Danger Level";
		body = "The current water level is in level 3 (DANGER) with a water level of " + waterLevel;

	} else if (waterLevel >= warningLevel) {
		title = "Warning Level";
		body = "The current water level is in level 2 (WARNING) with a water level of " + waterLevel;

	} else if (waterLevel >= alertLevel){
		title = "Alert Level";
		body = "The current water level is in level 1 (ALERT) with a water level of " + waterLevel;

	}
	
	const payload = {
		notification: {
			title: title,
			body: body
		}
	};
	
	const db = admin.firestore();
	const devicesRef = db.collection('devices').where("userId", "==", "testUser").get();

	// const tokens = [];
	// var token;
	// devicesRef.forEach(function (result) {
	// 	token = result.data().token;
	// 	tokens.push( token )
	// });

	// const newtoken = "f_Jj5XQP9x4:APA91bE9HMkm7qeGMdEAv59RQpYc28qSAzHhMPhx8nh2_6rLSI1Z-6Q6EiEr3iDmkivKlqqHAXJMrR4sQLOzGVu4Re5wuzf3w7ctaUjsRt4oS_VOJAZsGDcChPsznAGeSgeyASBj7yBU"

	return admin.messaging().sendToDevice(token, payload);
	
});
