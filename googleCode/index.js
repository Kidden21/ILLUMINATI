const functions = require('firebase-functions');
const admin = require('firebase-admin');

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
exports.helloWorld = functions.https.onRequest((request, response) => {
	console.log("hello")
	response.send("Hello from Kidden!");
});

exports.findItem = functions.https.onRequest((request, response) => {
	const serviceAccount = require("/Users/Kidden/Desktop/fit5120-ddc5582972f2.json");
	admin.initializeApp({
		credential: admin.credential.cert(serviceAccount)
	});
	const db = admin.firestore();
	const doc_ref = db.collection("BaganDatuk").doc("2011-2");
	const get_doc = doc_ref.get().then(doc => {
		if(!doc.exists){
			console.log("No such document!");
		} else {
			console.log("Document Data:", doc.data());
		}
	});	
});


// var serviceAccount = require('/Users/Kidden/Desktop/fit5120-ddc5582972f2.json');
//
// admin.initializeApp({
// 	credential: admin.credential.cert(serviceAccount)
// });
//
// var db = admin.firestore();
//
// var doc_ref = db.collection("BaganDatuk").doc("2011-2");
//
// var get_doc = doc_ref.get().then(doc => {
// 	if (!doc.exists){
// 		console.log('no such document!');
// 	} else {
// 		console.log("Document data:", doc.data());
// 	}
// })

// exports.addMessage = functions.https.onRequest((req, res) =>{
// 	const original = req.query.text;
// 	return admin.database().ref('/messages').push({original: original}).then((snapshot)=>{
// 		return res.redirect(303, snapshot.ref.toString());
// 	});
// });
//
// exports.makeUppercase - functions.database.ref('/messages/{pushId}/original').onCreate((snapshot, context) =>{
// 	const original = snapshot.val();
// 	console.log('Uppercasing', context.params.pushId, original);
// 	const uppercase = original.toUpperCase();
// 	return snapshot.ref.parent.child('uppercase').set(uppercase);
// });