const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp()

exports.createNewData = functions.firestore.document('zzchecking/{stationName}').onUpdate((change, context) => {
	const newValue = change.after.data();
	const waterLevel = newValue.Info.Water_Level;
	const alertLevel = newValue.Alert_System.Alert_Level;
	const warningLevel = newValue.Alert_System.Warning_Level;
	const dangerLevel = newValue.Alert_System.Danger_Level;
	const message = "The current water level is in DANGER level with a water level of ";
	
	if (waterLevel >= dangerLevel) {
		console.log(message + waterLevel);
	} else if (waterLevel >= warningLevel) {
		console.log(message + waterLevel);
	} else if (waterLevel >= alertLevel){
		console.log(message + waterLevel);
	}
	return message + waterLevel;
});

// exports.addMessage = functions.https.onRequest(async (req, res) =>{
// 	const original = req.query.text;
// 	const writeResult = await admin.firestore().collection('BaganDatuk/2010-1').add({original: original});
// 	res.json({result: 'Message with ID: ${writeResult.id} added.'});
//
	// return admin.database().ref('/messages').push({original: original}).then((snapshot)=>{
	// 	return res.redirect(303, snapshot.ref.toString());
	// 	});
// });
//
// exports.makeUppercase = functions.database.ref('/messages/{pushId}/original').onCreate((snapshot, context) =>{
// 	const original = snapshot.val();
// 	console.log('Uppercasing', context.params.pushId, original);
// 	const uppercase = original.toUpperCase();
// 	return snapshot.ref.parent.child('uppercase').set(uppercase);
// });

// Create and Deploy Your First Cloud Functions
// https://firebase.google.com/docs/functions/write-firebase-functions

// exports.helloWorld = functions.https.onRequest((request, response) => {
// 	console.log("hello")
// 	response.send("Hello from Kidden!");
// });


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



