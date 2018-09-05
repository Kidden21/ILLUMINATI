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
	//const message = locationValue + ", " + dateValue + ", " + timeValue + ": The current water level is in DANGER level with a water level of ";
	
	// const payload = {
	// 	notification: {
	// 		title: "Danger Level",
	// 		body: "The current water level is in DANGER level with a water level of "
	// 	}
	// };
	
	if (waterLevel >= dangerLevel) {
		//console.log(waterLevel);
		const payload = {
		notification: {
			title: "Danger Level",
			body: "The current water level is in level 3 (DANGER) with a water level of " + waterLevel
		}
	};
	} else if (waterLevel >= warningLevel) {
		//console.log(waterLevel);
		const payload = {
		notification: {
			title: "Danger Level",
			body: "The current water level is in level 2 (WARNING) with a water level of " + waterLevel
		}
	};
	} else if (waterLevel >= alertLevel){
		//console.log(waterLevel);
		const payload = {
		notification: {
			title: "Danger Level",
			body: "The current water level is in level 1 (ALERT) with a water level of " + waterLevel
		}
	};
	}
	
	// const db = admin.firestore();
	// const devicesRef = db.collection('devices').where("userId", "==", "testUser");
	//
	// const devices = devicesRef.get();
	
	// const tokens = [];

	// devices.forEach(function (result) {
	// 	const token = result.data().token;
	// 	tokens.push( token )
	// });

	const newtoken = "f_Jj5XQP9x4:APA91bE9HMkm7qeGMdEAv59RQpYc28qSAzHhMPhx8nh2_6rLSI1Z-6Q6EiEr3iDmkivKlqqHAXJMrR4sQLOzGVu4Re5wuzf3w7ctaUjsRt4oS_VOJAZsGDcChPsznAGeSgeyASBj7yBU"

	return admin.messaging().sendToDevice(newtoken, payload);
	
});

// var serviceAccount = require('/Users/Kidden/Desktop/fit5120-ddc5582972f2.json');
// admin.initializeApp({
// 	credential: admin.credential.cert(serviceAccount)
// });
// var db = admin.firestore();
// var doc_ref = db.collection("BaganDatuk").doc("2011-2");
// var get_doc = doc_ref.get().then(doc => {
// 	if (!doc.exists){
// 		console.log('no such document!');
// 	} else {
// 		console.log("Document data:", doc.data());
// 	}
// })



