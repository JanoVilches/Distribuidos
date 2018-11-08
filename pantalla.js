var PROTO_PATH = __dirname + '/../Proto/Aeropuerto.proto';

var async = require('async');
var fs = require('fs');
var parseArgs = require('minimist');
var path = require('path');
var _ = require('lodash');
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var aeropuerto = grpc.loadPackageDefinition(packageDefinition);

var client = new Torre('localhost:50051',
                                       grpc.credentials.createInsecure());
