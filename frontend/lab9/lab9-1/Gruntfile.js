module.exports = function(grunt){
	grunt.initConfig({
		compass: {
			dist: {
				options: {
					sassDir : 'dev/css/sass',
					cssDir : 'dist/css',
					environment : 'production'
				}
			},
			dev: {
				options: {
					sassDir : 'dev/css/sass',
					cssDir : 'dev/css/stylesheets'
				}
			}
		}
	});

	grunt.loadNpmTasks('grunt-contrib-compass');

	grunt.registerTask("default", ['compass']);
}